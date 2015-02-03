from effect_runner import PerformEffects
from Game.Events.cards_event import CardsEvent

class PerMatch:
    """ Represents an effect that applies for each matching card """
    
    def __init__(self, zoneType, effects, filter=None):
        """ Initialize the Effect with the condition to evaluate and effect to perform """
        self.zoneType = zoneType
        self.effects = effects
        self.filter = filter
        
    def perform(self, context):
        """ Perform the Game Effect """
        zone, cards = self.findPossibleCards(context)
        for card in cards:
            event = CardsEvent([card], zone, context)
            coroutine = PerformEffects(self.effects, event.context)
            try:
                response = yield coroutine.next()
                while True:
                    response = yield coroutine.send(response)
            except StopIteration:
                pass
                
    def findPossibleCards(self, context):
        """ Return the possible cards """
        zone = context.loadZone(self.zoneType)
        possibleCards = zone
        if self.filter is not None:
            possibleCards = self.filter.evaluate(context)
        
        return zone, possibleCards