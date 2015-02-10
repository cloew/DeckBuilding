from Server.helpers.json_factory import jsonFactory
from Server.Lobby.lobbies import lobbies, lobbyIdToPlayers
from kao_flask.controllers.json_controller import JSONController

class ChangeCharacterController(JSONController):
    """ Controller to handle creating a new Game Lobby via JSON """
    
    def performWithJSON(self, lobbyId, playerId, json=None):
        currentPlayer=lobbyIdToPlayers[lobbyId][playerId]
        currentPlayer.setCharacter(json['character'])
        return jsonFactory.toJson(lobbies[lobbyId], playerId=playerId, currentPlayer=currentPlayer), 201