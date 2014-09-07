
class ConditionalEffect:
    """ Represents an effect that conditionally applies """
    
    def __init__(self, condition, effect):
        """ Initialize the Effect with the condition to evaluate and effect to perform """
        self.condition = condition
        self.effect = effect
        
    def perform(self, owner, card, game):
        """ Perform the Game Effect """
        if self.condition.evaluate(game):
            self.effect.perform(owner, card, game)