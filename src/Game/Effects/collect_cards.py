from Game.Effects.effect_runner import PerformEffects
from Game.Events.cards_event import CardsEvent
from Game.Sources.source_factory import DECK

class CollectCards:
    """ Represents an effect to Collect Cards from the top of your opponents decks """
    
    def __init__(self, thenEffects, sourceType=None):
        """ Initialize the Effect with the effects to call with the collected cards """
        self.thenEffects = thenEffects
        if sourceType is None:
            sourceType = DECK
        self.sourceType = sourceType
        
    def perform(self, context):
        """ Perform the Game Effect """
        collectedCards = [context.getPlayerContext(foe).loadSource(self.sourceType)[0] for foe in context.foes]
                
        event = CardsEvent(collectedCards, None, context)
        coroutine = PerformEffects(self.thenEffects, event.context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)