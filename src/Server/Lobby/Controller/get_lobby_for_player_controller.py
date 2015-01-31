from Server.Lobby.lobbies import lobbies
from kao_flask.controllers.json_controller import JSONController

class GetLobbyForPlayerController(JSONController):
    """ Controller to return basic lobby details """
    
    def performWithJSON(self, lobbyId, playerId, json=None):
        return lobbies[lobbyId].toJSONForPlayer(playerId)