from Server.Game.games import games

from Server.Game.Controller.game_command_controller import GameCommandController

class GameResponseController(GameCommandController):
    """ Controller to perform a game response command """
        
    def performCommand(self, game, command):
        """ Perform the given command """
        command.perform()