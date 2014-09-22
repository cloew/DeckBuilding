from Game.Commands.Responses.choose_option import ChooseOption
from Server.Game.games import games

from kao_flask.controllers.json_controller import JSONController

class ChooseController(JSONController):
    """ Controller to choose an option """
    
    def performWithJSON(self, gameId, playerId):
        game = games[gameId]
        optionIndex = self.json['index']
        option = game.game.currentTurn.request.options[optionIndex]
        ChooseOption(option, game.game.currentTurn).perform()
        return game.toJSONForPlayer(playerId)