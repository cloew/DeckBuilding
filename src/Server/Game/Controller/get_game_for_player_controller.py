from Server.helpers.json_factory import jsonFactory
from Server.Game.games import games, gameToPlayers
from kao_flask.controllers.json_controller import JSONController

class GetGameForPlayerController(JSONController):
    """ Controller to return game details for the particular player """
    
    def performWithJSON(self, gameId, playerId, json=None):
        return {'game':jsonFactory.toJson(games[gameId], gameId=gameId, playerId=playerId, currentPlayer=gameToPlayers[gameId][playerId])}