from Game.Commands.end_turn import EndTurn
from Server.Game.games import games

from Server.Game.Controller.game_command_controller import GameCommandController

class EndTurnController(GameCommandController):
    """ Controller to end the current turn """
        
    def buildCommand(self, player, game, json):
        """ Build the Command to try and perform """
        return EndTurn(game)