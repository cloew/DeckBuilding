
class OrCondition:
    """ Represents a condition where any of the conditions must be true """
    
    def __init__(self, conditions):
        """ Initialize the Or Condition with the conditions to check """
        self.conditions = conditions
        
    def evaluate(self, context):
        """ Evaluate the condition """
        return any([condition.evaluate(context) for condition in self.conditions])
        