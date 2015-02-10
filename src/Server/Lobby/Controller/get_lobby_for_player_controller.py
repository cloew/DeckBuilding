from Server.helpers.json_factory import jsonFactory
from Server.Lobby.lobbies import lobbies, lobbyIdToPlayers
from kao_flask.controllers.json_controller import JSONController

class GetLobbyForPlayerController(JSONController):
    """ Controller to return basic lobby details """
    
    def performWithJSON(self, lobbyId, playerId, json=None):
        return jsonFactory.toJson(lobbies[lobbyId], playerId=playerId, currentPlayer=lobbyIdToPlayers[lobbyId][playerId])