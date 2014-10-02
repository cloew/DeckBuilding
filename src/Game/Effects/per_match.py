from effect_runner import PerformEffect

from Game.Effects.Conditions.Filters.comparison_filter import ComparisonFilter
from Game.Events.cards_event import CardsEvent
from Game.Sources.source_factory import SourceFactory

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
        source = SourceFactory.getSourceForEffect(self.sourceType, context)
        possibleCards = source
        if self.filter is not None:
            possibleCards = self.filter.evaluate(context)
        
        return source, possibleCards