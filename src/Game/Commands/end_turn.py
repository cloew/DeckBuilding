
class EndTurn:
    """ Represents a Command to end the turn """
    
    def __init__(self, game):
        """ Initialize the Command """
        self.game = game
        
    def perform(self):
        """ Perform the command """
        self.game.endTurn()