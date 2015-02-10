from Server.helpers.json_factory import jsonFactory
from Server.Game.games import games, gameToPlayers
from kao_flask.controllers.json_controller import JSONController

class GetResultsForPlayerController(JSONController):
    """ Controller to return game results for the particular player """
    
    def performWithJSON(self, gameId, playerId, json=None):
        return jsonFactory.toJson(games[gameId].results, game=games[gameId], playerId=playerId, currentPlayer=gameToPlayers[gameId][playerId])