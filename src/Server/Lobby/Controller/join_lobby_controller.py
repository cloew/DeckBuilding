from Server.helpers.json_factory import jsonFactory
from Server.Lobby.lobbies import AddPlayerToLobby
from kao_flask.controllers.json_controller import JSONController

class JoinLobbyController(JSONController):
    """ Controller to handle creating a new Game Lobby via JSON """
    
    def performWithJSON(self, lobbyId, json=None):
        playerId = AddPlayerToLobby(lobbyId)
        return {'playerId':playerId, 'lobbyId':lobbyId}, 201