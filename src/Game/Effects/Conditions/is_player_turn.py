
class IsPlayerTurn:
    """ Represents a condition where a source must have cards """
    
    def __init__(self):
        """ Initialize the Condition with the Source to check that has cards """
        
    def evaluate(self, context):
        """ Evaluate the condition """
        return context.player is context.owner.player
        