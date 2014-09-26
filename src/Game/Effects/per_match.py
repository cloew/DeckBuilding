from effect_runner import PerformEffect

from Game.Effects.Conditions.Filters.comparison_filter import ComparisonFilter
from Game.Events.cards_event import CardsEvent
from Game.Sources.source_factory import SourceFactory

class PerMatch:
    """ Represents an effect that applies for each matching card """
    
    def __init__(self, sourceType, filter, effect):
        """ Initialize the Effect with the condition to evaluate and effect to perform """
        self.sourceType = sourceType
        self.filter = filter
        self.effect = effect
        
    def perform(self, args):
        """ Perform the Game Effect """
        source = SourceFactory.getSourceForEffect(self.sourceType, args)
        for card in self.filter.evaluate(args):
            event = CardsEvent([card], source, args)
            coroutine = PerformEffect(self.effect, event.args)
            try:
                response = yield coroutine.next()
                while True:
                    response = yield coroutine.send(response)
            except StopIteration:
                pass