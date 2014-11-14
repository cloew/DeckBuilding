
class WinGame:
    """ Represents an effect to Win the Game """
        
    def perform(self, context):
        """ Perform the Game Effect """
        context.game.endAfterThisTurn()