from Game.Effects.Conditions.filter import Filter

class PerMatch:
    """ Represents an effect that applies for each matching card """
    
    def __init__(self, field, values, sourceType, effect):
        """ Initialize the Effect with the condition to evaluate and effect to perform """
        self.filter = Filter(field, values, sourceType, "IN")
        self.effect = effect
        
    def perform(self, args):
        """ Perform the Game Effect """
        for card in self.filter.evaluate(args.game, event=args.event):
            self.effect.perform(args)