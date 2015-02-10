from Server.helpers.json_factory import jsonFactory
from Server.Lobby.lobbies import lobbies
from kao_flask.controllers.json_controller import JSONController

class GetLobbiesController(JSONController):
    """ Controller to return all lobbies """
    
    def performWithJSON(self, json=None):
        return {'lobbies':jsonFactory.toJson([lobby for lobby in lobbies.values()])}