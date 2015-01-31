from Server.Game.games import games
from kao_flask.controllers.json_controller import JSONController

class GetGameController(JSONController):
    """ Controller to return basic game details """
    
    def performWithJSON(self, gameId, json=None):
        return games[gameId].toJSON()