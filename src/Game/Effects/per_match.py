from Game.Effects.Conditions.Filters.comparison_filter import ComparisonFilter

class PerMatch:
    """ Represents an effect that applies for each matching card """
    
    def __init__(self, sourceType, criteria, effect):
        """ Initialize the Effect with the condition to evaluate and effect to perform """
        self.filter = ComparisonFilter(sourceType, criteria)
        self.effect = effect
        
    def perform(self, args):
        """ Perform the Game Effect """
        for card in self.filter.evaluate(args.game, event=args.event):
            self.effect.perform(args)