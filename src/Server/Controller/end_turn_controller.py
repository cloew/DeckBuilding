from Game.Commands.end_turn import EndTurn
from Server.Game.game_wrapper import GameWrapper

from kao_flask.controllers.json_controller import JSONController

class EndTurnController(JSONController):
    """ Controller to end the current turn """
    
    def performWithJSON(self, gameId):
        game = GameWrapper(id=gameId)
        EndTurn(game.game).perform()
        return game.toJSON()