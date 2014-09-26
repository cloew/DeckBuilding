from Game.Effects.effect_arguments import EffectArguments
from Game.Effects.Conditions.Filters.comparison_filter import ComparisonFilter
from Game.Events.cards_event import CardsEvent
from Game.Sources.source_factory import SourceFactory

class PerMatch:
    """ Represents an effect that applies for each matching card """
    
    def __init__(self, sourceType, criteria, effect):
        """ Initialize the Effect with the condition to evaluate and effect to perform """
        self.filter = ComparisonFilter(sourceType, criteria)
        self.effect = effect
        
    def perform(self, args):
        """ Perform the Game Effect """
        source = SourceFactory.getSourceForEffect(self.filter.sourceType, args)
        for card in self.filter.evaluate(args):
            event = CardsEvent([card], source, args)
            self.effect.perform(event.args)