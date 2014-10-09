from Game.coroutine_helper import RunCoroutineOrFunction
from Game.Commands.Requests.pick_card_request import PickCardRequest
from Game.Effects.effect_runner import PerformEffects
from Game.Events.cards_event import CardsEvent
from Game.Sources.source_types import DECK

PICK = "PICK"
TOP = "TOP"

class CollectCards:
    """ Represents an effect to Collect Cards from the top of your opponents decks """
    
    def __init__(self, thenEffects, sourceType=None, pickType=None, number=None):
        """ Initialize the Effect with the effects to call with the collected cards """
        self.thenEffects = thenEffects
        if sourceType is None:
            sourceType = DECK
        self.sourceType = sourceType
        if pickType is None:
            pickType = TOP
        self.pickType = pickType
        if number is None:
            number = 1
        self.number = number
        
    def perform(self, context):
        """ Perform the Game Effect """
        typeToFunction = {TOP:self.getTopCards,
                          PICK:self.pickCards}
        function = typeToFunction[self.pickType]
        
        self.cardsForFoes = []
        collectedCards = []
        for foe in context.foes:
            coroutine = RunCoroutineOrFunction(function, [context, context.getPlayerContext(foe).loadSource(self.sourceType), self.number])
            try:
                response = yield coroutine.next()
                while True:
                    response = yield coroutine.send(response)
            except StopIteration:
                pass
            collectedCards += self.cardsForFoes
                
        event = CardsEvent(collectedCards, None, context)
        coroutine = PerformEffects(self.thenEffects, event.context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)
            
    def getTopCards(self, context, source, number):
        """ Get the Top Cards """
        self.cardsForFoes = source[:number]
            
    def pickCards(self, context, source, number):
        """ Get the Top Cards """
        self.cardsForFoes = yield PickCardRequest(source, context.player, number)
        