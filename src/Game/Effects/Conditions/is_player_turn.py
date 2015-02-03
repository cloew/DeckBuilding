
class IsPlayerTurn:
    """ Represents a condition where it must be the asking players turn """
        
    def evaluate(self, context):
        """ Evaluate the condition """
        return context.player is context.owner.player
        