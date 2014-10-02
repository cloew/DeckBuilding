from Game.Effects.effect_runner import PerformEffects
from Game.Events.cards_event import CardsEvent

class Filter:
    """ Represents an effect to pick cards from a source and an optional filter """
    
    def __init__(self, sourceType, filter, thenEffects):
        """ Initialize the options """
        self.sourceType = sourceType
        self.filter = filter
        self.thenEffects = thenEffects
        
    def perform(self, context):
        """ Perform the Game Effect """
        source = context.loadSource(self.sourceType)
        possibleCards = self.filter.evaluate(context)
                
        event = CardsEvent(possibleCards, source, context)
        coroutine = PerformEffects(self.thenEffects, event.context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)