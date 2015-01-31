from Server.Game.games import games
from kao_flask.controllers.json_controller import JSONController

class GetResultsForPlayerController(JSONController):
    """ Controller to return game results for the particular player """
    
    def performWithJSON(self, gameId, playerId, json=None):
        return games[gameId].toResultJSONForPlayer(playerId)