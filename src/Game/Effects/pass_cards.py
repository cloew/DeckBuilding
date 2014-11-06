from Game.Commands.Requests.pick_card_request import PickCardRequest
from Game.Effects.move_card import MoveCard
from Game.Effects.effect_runner import PerformEffect
from Game.Events.cards_event import CardsEvent
from Game.Sources.list_source import ListSource
from Game.Sources.source_types import HAND, EVENT

class CardsToPass:
    """ Represents the cards that should be passed form one player to another """
    
    def __init__(self, cardsSource, targetPlayer):
        """ Initialize the cards to pass with the target player and the cards """
        self.cardsSource = cardsSource
        self.targetPlayer = targetPlayer
        
    def passCards(self, context):
        """ Pass the cards to the target player """
        event = CardsEvent(self.cardsSource.cards, self.cardsSource, context.getPlayerContext(self.targetPlayer))
        return PerformEffect(MoveCard(EVENT, HAND), event.context)

class PassCards:
    """ Represents an effect to Pass Cards between players """
    
    def __init__(self, sourceType):
        """ Initialize the Effect with the source to pass from """
        self.sourceType = sourceType
        
    def perform(self, context):
        """ Perform the Game Effect """
        allCardsToPass = []
        sources = []
        for foe in context.foes:
            playerContext = context.getPlayerContext(foe)
            source = playerContext.loadSource(self.sourceType)
            
            for toDescription, target in zip(["pass to the previous player", "pass to the next player"], [playerContext.previousPlayer, playerContext.nextPlayer]):
                cards = yield PickCardRequest(source, foe, 1, toDescription)
                
                event = CardsEvent(cards, source, playerContext)
                placeholderSource = ListSource([])
                MoveCard(EVENT, HAND).moveCards(event.context.loadSource(EVENT), placeholderSource)
                
                cardsToPass = CardsToPass(placeholderSource, target)
                allCardsToPass.append(cardsToPass)
                
        for cardsToPass in allCardsToPass:
            coroutine = cardsToPass.passCards(context)
            try:
                response = yield coroutine.next()
                while True:
                    response = yield coroutine.send(response)
            except StopIteration:
                pass