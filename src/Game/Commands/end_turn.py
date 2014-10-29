from command import Command

from Game.Commands.Requirements.current_player import CurrentPlayer
from Game.Commands.Requirements.no_request import NoRequest

class EndTurn(Command):
    """ Represents a Command to end the turn """
    
    def __init__(self, game):
        """ Initialize the Command """
        self.game = game
        Command.__init__(self, [CurrentPlayer(), NoRequest()])
        
    def perform(self):
        """ Perform the command """
        self.game.endTurn()