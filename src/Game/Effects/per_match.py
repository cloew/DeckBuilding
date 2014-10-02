from effect_runner import PerformEffect
from Game.Events.cards_event import CardsEvent

class PerMatch:
    """ Represents an effect that applies for each matching card """
    
    def __init__(self, sourceType, effect, filter=None):
        """ Initialize the Effect with the condition to evaluate and effect to perform """
        self.sourceType = sourceType
        self.effect = effect
        self.filter = filter
        
    def perform(self, context):
        """ Perform the Game Effect """
        source, cards = self.findPossibleCards(context)
        for card in cards:
            event = CardsEvent([card], source, context)
            coroutine = PerformEffect(self.effect, event.context)
            try:
                response = yield coroutine.next()
                while True:
                    response = yield coroutine.send(response)
            except StopIteration:
                pass
                
    def findPossibleCards(self, context):
        """ Return the possible cards """
        source = context.loadSource(self.sourceType)
        possibleCards = source
        if self.filter is not None:
            possibleCards = self.filter.evaluate(context)
        
        return source, possibleCards