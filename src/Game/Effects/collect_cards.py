from Game.coroutine_helper import RunCoroutineOrFunction
from Game.Commands.Requests.pick_card_request import PickCardRequest
from Game.Effects.effect_runner import PerformEffects
from Game.Events.cards_event import CardsEvent
from Game.Events.multi_source_event import MultiSourceEvent
from Game.Sources.event_source import EventSource
from Game.Sources.source_types import DECK

PICK = "PICK"
TOP = "TOP"

class CollectCards:
    """ Represents an effect to Collect Cards from the top of your opponents decks """
    
    def __init__(self, thenEffects, sourceType=None, pickType=None, number=None, toDescription=None):
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
        
        if toDescription is None:
            toDescription = ""
        self.toDescription = toDescription
        
    def perform(self, context):
        """ Perform the Game Effect """
        typeToFunction = {TOP:self.getTopCards,
                          PICK:self.pickCards}
        function = typeToFunction[self.pickType]
        
        self.cardsForFoes = []
        sources = []
        for foe in context.foes:
            playerContext = context.getPlayerContext(foe)
            source = playerContext.loadSource(self.sourceType)
            coroutine = RunCoroutineOrFunction(function, [playerContext, source, self.number])
            try:
                response = yield coroutine.next()
                while True:
                    response = yield coroutine.send(response)
            except StopIteration:
                pass
            event = CardsEvent(self.cardsForFoes, source, playerContext)
            sources.append(EventSource(event))
                
        event = MultiSourceEvent(sources, context)
        coroutine = PerformEffects(self.thenEffects, event.context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)
            
    def getTopCards(self, context, source, number):
        """ Get the Top Cards """
        self.cardsForFoes = source[:number]
            
    def pickCards(self, context, source, number):
        """ Get the Top Cards """
        self.cardsForFoes = yield PickCardRequest(source, context.player, number, self.toDescription)
        