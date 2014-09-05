from Server.game_wrapper import GameWrapper
from kao_flask.controllers.json_controller import JSONController

class StartNextRoundController(JSONController):
    """ Controller to begin the Next Round """
    
    def performWithJSON(self, gameId):
        game = GameWrapper(id=gameId)
        game.startNextRound()
        return game.toJSON()
        