
class AndCondition:
    """ Represents a condition where all the conditions must be true """
    
    def __init__(self, conditions):
        """ Initialize the And Condition with the conditions to check """
        self.conditions = conditions
        
    def evaluate(self, game, event=None):
        """ Evaluate the condition """
        return all([condition.evaluate(game, event=event) for condition in self.conditions])
        