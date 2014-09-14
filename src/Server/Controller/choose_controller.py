from Game.Commands.Responses.choose_option import ChooseOption
from Server.Game.game_wrapper import GameWrapper

from kao_flask.controllers.json_controller import JSONController

class ChooseController(JSONController):
    """ Controller to choose an option """
    
    def performWithJSON(self, gameId):
        game = GameWrapper(id=gameId)
        optionIndex = self.json['index']
        option = game.game.currentTurn.request.options[optionIndex]
        ChooseOption(option, game.game.currentTurn).perform()
        return game.toJSON()