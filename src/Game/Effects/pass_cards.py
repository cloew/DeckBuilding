from Game.Commands.Requests.pick_card_request import PickCardRequest
from Game.Effects.move_card import MoveCard
from Game.Effects.effect_runner import PerformEffect
from Game.Events.cards_event import CardsEvent
from Game.Zones.list_zone import ListZone
from Game.Zones.zone_types import HAND, EVENT

class CardsToPass:
    """ Represents the cards that should be passed form one player to another """
    
    def __init__(self, cardsZone, targetPlayer):
        """ Initialize the cards to pass with the target player and the cards """
        self.cardsZone = cardsZone
        self.targetPlayer = targetPlayer
        
    def passCards(self, context):
        """ Pass the cards to the target player """
        event = CardsEvent(self.cardsZone.cards, self.cardsZone, context.getPlayerContext(self.targetPlayer))
        return PerformEffect(MoveCard(EVENT, HAND), event.context)

class PassCards:
    """ Represents an effect to Pass Cards between players """
    
    def __init__(self, zoneType):
        """ Initialize the Effect with the zone to pass from """
        self.zoneType = zoneType
        
    def perform(self, context):
        """ Perform the Game Effect """
        allCardsToPass = []
        zones = []
        for foe in context.foes:
            playerContext = context.getPlayerContext(foe)
            zone = playerContext.loadZone(self.zoneType)
            
            for toDescription, target in zip(["pass to the previous player", "pass to the next player"], [playerContext.previousPlayer, playerContext.nextPlayer]):
                cards = yield PickCardRequest(zone, foe, 1, toDescription)
                
                event = CardsEvent(cards, zone, playerContext)
                placeholderZone = ListZone([])
                MoveCard(EVENT, HAND).moveCards(event.context.loadZone(EVENT), placeholderZone)
                
                cardsToPass = CardsToPass(placeholderZone, target)
                allCardsToPass.append(cardsToPass)
                
        for cardsToPass in allCardsToPass:
            coroutine = cardsToPass.passCards(context)
            try:
                response = yield coroutine.next()
                while True:
                    response = yield coroutine.send(response)
            except StopIteration:
                pass