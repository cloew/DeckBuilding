from Game.Commands.Requests.pick_card_request import PickCardRequest

from Game.Effects.effect_runner import PerformEffects
from Game.Effects.conditional_effect import ConditionalEffect

from Game.Effects.Conditions.has_cards import HasCards
from Game.Effects.Conditions.or_condition import OrCondition
from Game.Effects.Conditions.Filters.comparison_filter import ComparisonFilter
from Game.Effects.Conditions.Filters.intersection_filter import IntersectionFilter

from Game.Events.cards_event import CardsEvent
from Game.Events.multi_zone_event import MultiZoneEvent

from Game.Zones.event_zone import EventZone

class PickCards(ConditionalEffect):
    """ Represents an effect to pick cards from a zone and an optional filter """
    REQUEST_CLASS = PickCardRequest
    AUTO_PICK = True
    
    def __init__(self, zoneTypes, numberOfCards, toDescription, thenEffects, criteria=None, leftoverCardEffects=[]):
        """ Initialize the options """
        self.zoneTypes = zoneTypes
        self.numberOfCards = numberOfCards
        self.toDescription = toDescription
        self.leftoverCardEffects = leftoverCardEffects
        
        self.filters = None
        if criteria is not None:
            self.filters = []
            for zoneType in zoneTypes:
                self.filters.append(IntersectionFilter([ComparisonFilter(zoneType, c) for c in criteria]))
            
        conditions = []
        for zoneType in zoneTypes:
            filter = None
            if self.filters is not None:
                filter=self.filters[zoneTypes.index(zoneType)]
            conditions.append(HasCards(zoneType, filter=filter))
        condition = OrCondition(conditions)
        
        ConditionalEffect.__init__(self, condition, thenEffects)
        
    def performEffects(self, context):
        """ Perform the Game Effect """
        possibleCardsPerZone = self.findPossibleCards(context)
        possibleCards = [card for cards in possibleCardsPerZone.values() for card in cards]
        
        if len(possibleCards) != 0:
            cards = None
            if len(possibleCards) == self.numberOfCards and self.AUTO_PICK:
                cards = possibleCards
            else:
                cards = yield self.buildRequest(possibleCards, context)
                
            event = self.buildEvent(cards, possibleCardsPerZone, context)
        
        coroutine = ConditionalEffect.performEffects(self, event.context)
        try:
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response)
        except StopIteration:
            pass
        
        coroutine = PerformEffects(self.leftoverCardEffects, self.buildEvent([card for card in possibleCards if card not in cards], possibleCardsPerZone, context).context)
        try:
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response)
        except StopIteration:
            pass
            
    def buildRequest(self, possibleCards, context):
        """ Build the Request """
        return self.REQUEST_CLASS(possibleCards, context.player, self.numberOfCards, self.toDescription)
                
    def findPossibleCards(self, context):
        """ Return the possible cards """
        zones = [context.loadZone(zoneType) for zoneType in self.zoneTypes]
        possibleCards = {}
        for zone in zones:
            possibleCards[zone] = zone
            if self.filters is not None:
                possibleCards[zone] = self.filters[zones.index(zone)].evaluate(context)
        
        return possibleCards
        
    def buildEvent(self, cards, possibleCardsPerZone, context):
        """ Build the proper event for the chosen cards """
        cardsPerZone = {}
        for card in cards:
            for zone in possibleCardsPerZone:
                if card in zone:
                    if zone in cardsPerZone:
                        cardsPerZone[zone].append(card)
                    else:
                        cardsPerZone[zone] = [card]
                    break
                    
        zones = [CardsEvent(cardsPerZone[zone], zone, context).loadZone() for zone in cardsPerZone]
        return MultiZoneEvent(zones, context)
        
    def setNumberOfCards(self, number):
        """ Set the Number of Cards that can be requested """
        self.numberOfCards = number