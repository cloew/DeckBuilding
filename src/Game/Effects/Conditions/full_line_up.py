
class FullLineUp:
    """ Represents a condition where the Line Up must be full """
        
    def evaluate(self, args):
        """ Evaluate the condition """
        return args.game.lineUp.isFull()