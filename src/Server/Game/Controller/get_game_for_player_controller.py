from Server.Game.games import games
from kao_flask.controllers.json_controller import JSONController

class GetGameForPlayerController(JSONController):
    """ Controller to return game details for the particular player """
    
    def performWithJSON(self, gameId, playerId, json=None):
        return games[gameId].toJSONForPlayer(playerId)