from Server.game_wrapper import GameWrapper
from kao_flask.controllers.json_controller import JSONController

class GetGameController(JSONController):
    """ Controller to return basic game details """
    
    def performWithJSON(self, gameId):
        return GameWrapper(id=gameId).toJSON()