from Game.Commands.end_turn import EndTurn
from Server.Game.games import games

from kao_flask.controllers.json_controller import JSONController

class EndTurnController(JSONController):
    """ Controller to end the current turn """
    
    def performWithJSON(self, gameId, playerId):
        game = games[gameId]
        game.game.currentTurn.perform(EndTurn(game.game))
        return game.toJSONForPlayer(playerId)