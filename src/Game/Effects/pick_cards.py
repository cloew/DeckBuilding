from Game.Commands.Requests.pick_card_request import PickCardRequest
from Game.Effects.conditional_effect import ConditionalEffect
from Game.Effects.Conditions.has_cards import HasCards
from Game.Effects.Conditions.or_condition import OrCondition
from Game.Effects.Conditions.Filters.comparison_filter import ComparisonFilter
from Game.Effects.Conditions.Filters.intersection_filter import IntersectionFilter
from Game.Events.cards_event import CardsEvent
from Game.Events.multi_source_event import MultiSourceEvent
from Game.Sources.event_source import EventSource

class PickCards(ConditionalEffect):
    """ Represents an effect to pick cards from a source and an optional filter """
    REQUEST_CLASS = PickCardRequest
    AUTO_PICK = True
    
    def __init__(self, sourceTypes, numberOfCards, thenEffects, criteria=None):
        """ Initialize the options """
        self.sourceTypes = sourceTypes
        self.numberOfCards = numberOfCards
        
        self.filters = None
        if criteria is not None:
            self.filters = []
            for sourceType in sourceTypes:
                self.filters.append(IntersectionFilter([ComparisonFilter(sourceType, c) for c in criteria]))
            
        conditions = []
        for sourceType in sourceTypes:
            filter = None
            if self.filters is not None:
                filter=self.filters[sourceTypes.index(sourceType)]
            conditions.append(HasCards(sourceType, filter=filter))
        condition = OrCondition(conditions)
        
        ConditionalEffect.__init__(self, condition, thenEffects)
        
    def performEffects(self, context):
        """ Perform the Game Effect """
        possibleCardsPerSource = self.findPossibleCards(context)
        possibleCards = [card for cards in possibleCardsPerSource.values() for card in cards]
        
        if len(possibleCards) != 0:
            card = None
            if len(possibleCards) == self.numberOfCards and self.AUTO_PICK:
                cards = possibleCards
            else:
                cards = yield self.REQUEST_CLASS(possibleCards, context.player, self.numberOfCards)
                
            event = self.buildEvent(cards, possibleCardsPerSource, context)
        
        coroutine = ConditionalEffect.performEffects(self, event.context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)
                
    def findPossibleCards(self, context):
        """ Return the possible cards """
        sources = [context.loadSource(sourceType) for sourceType in self.sourceTypes]
        possibleCards = {}
        for source in sources:
            possibleCards[source] = source
            if self.filters is not None:
                possibleCards[source] = self.filters[sources.index(source)].evaluate(context)
        
        return possibleCards
        
    def buildEvent(self, cards, possibleCardsPerSource, context):
        """ Build the proper event for the chosen cards """
        cardsPerSource = {}
        for card in cards:
            for source in possibleCardsPerSource:
                if card in source:
                    if source in cardsPerSource:
                        cardsPerSource[source].append(card)
                    else:
                        cardsPerSource[source] = [card]
                    break
                    
        sources = [EventSource(CardsEvent(cardsPerSource[source], source, context)) for source in cardsPerSource]
        return MultiSourceEvent(sources, context)
        
    def setNumberOfCards(self, number):
        """ Set the Number of Cards that can be requested """
        self.numberOfCards = number