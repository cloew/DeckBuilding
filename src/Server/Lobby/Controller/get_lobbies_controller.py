from Server.Lobby.lobbies import lobbies
from kao_flask.controllers.json_controller import JSONController

class GetLobbiesController(JSONController):
    """ Controller to return all lobbies """
    
    def performWithJSON(self):
        return {'lobbies':[lobby.toJSON() for lobby in lobbies.values()]}