from Game.Commands.Responses.choose_option import ChooseOption

from Server.Game.Controller.game_command_controller import GameCommandController

class ChooseController(GameCommandController):
    """ Controller to choose an option """
        
    def buildCommand(self, player, game, json):
        """ Build the Command to try and perform """
        optionIndex = self.json['index']
        
        command = None
        if game.currentTurn.request is not None and optionIndex < len(game.currentTurn.request.options):
            option = game.currentTurn.request.options[optionIndex]
            command = ChooseOption(option, game.game.currentTurn)
        return command