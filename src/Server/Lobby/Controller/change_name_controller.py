from Server.helpers.json_factory import jsonFactory
from Server.Lobby.lobbies import lobbies, lobbyIdToPlayers
from kao_flask.controllers.json_controller import JSONController

class ChangeNameController(JSONController):
    """ Controller to handle changing a player's name via JSON """
    
    def performWithJSON(self, lobbyId, playerId, json=None):
        currentPlayer=lobbyIdToPlayers[lobbyId][playerId]
        currentPlayer.setName(json['name'])
        return jsonFactory.toJson(lobbies[lobbyId], playerId=playerId, currentPlayer=currentPlayer), 201