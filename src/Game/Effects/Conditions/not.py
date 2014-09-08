
class Not:
    """ Represents a condition where a condition must not be true """
    
    def __init__(self, condition):
        """ Initialize the Not Condition with the condition that must not be true """
        self.condition = condition
        
    def evaluate(self, game, event=None):
        """ Evaluate the condition """
        return not self.condition.evaluate(game, event=event)
        