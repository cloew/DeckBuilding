from Server.helpers.json_factory import jsonFactory
from Server.Lobby.lobbies import lobbies, lobbyIdToPlayers
from kao_flask.controllers.json_controller import JSONController

class ChangeNumberOfVillainsController(JSONController):
    """ Controller to handle changing the number of villains via JSON """
    
    def performWithJSON(self, lobbyId, playerId, json=None):
        lobby = lobbies[lobbyId]
        currentPlayer=lobbyIdToPlayers[lobbyId][playerId]
        lobby.gameMode.setNumberOfVillains(json['index'])
        return jsonFactory.toJson(lobbies[lobbyId], playerId=playerId, currentPlayer=currentPlayer), 201