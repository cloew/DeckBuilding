
class FullLineUp:
    """ Represents a condition where the Line Up must be full """
        
    def evaluate(self, context):
        """ Evaluate the condition """
        return context.game.lineUp.isFull()