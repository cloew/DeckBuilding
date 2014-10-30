from Game.Commands.Responses.choose_option import ChooseOption

from Server.Game.Controller.game_command_controller import GameCommandController

class ChooseController(GameCommandController):
    """ Controller to choose an option """
        
    def buildCommand(self, player, game, json):
        """ Build the Command to try and perform """
        optionIndex = self.json['index']
        return ChooseOption(optionIndex, game.currentTurn)