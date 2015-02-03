from Game.Effects.effect_runner import PerformEffects
from Game.Events.cards_event import CardsEvent

class Filter:
    """ Represents an effect to pick cards from a zone and an optional filter """
    
    def __init__(self, zoneType, filter, thenEffects):
        """ Initialize the options """
        self.zoneType = zoneType
        self.filter = filter
        self.thenEffects = thenEffects
        
    def perform(self, context):
        """ Perform the Game Effect """
        zone = context.loadZone(self.zoneType)
        possibleCards = self.filter.evaluate(context)
                
        event = CardsEvent(possibleCards, zone, context)
        coroutine = PerformEffects(self.thenEffects, event.context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)