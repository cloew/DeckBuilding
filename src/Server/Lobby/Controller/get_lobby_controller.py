from Server.Lobby.lobbies import lobbies
from kao_flask.controllers.json_controller import JSONController

class GetLobbyController(JSONController):
    """ Controller to return basic lobby details """
    
    def performWithJSON(self, lobbyId):
        return lobbies[lobbyId].toJSON()