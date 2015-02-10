from Game.Decks.deck_roles import STARTING
from Server.helpers.json_factory import jsonFactory
from Server.Lobby.lobbies import lobbies, lobbyIdToPlayers
from kao_flask.controllers.json_controller import JSONController

class ChangeDeckForRoleController(JSONController):
    """ Controller to handle changing the Deck for a particular role via JSON """
    
    def performWithJSON(self, lobbyId, playerId, json=None):
        lobby = lobbies[lobbyId]
        currentPlayer=lobbyIdToPlayers[lobbyId][playerId]
        role = json['role']
        index = json['index']
        
        if role == STARTING:
            currentPlayer.setDeck(index)
        else:
            lobby.gameMode.setDeckForRole(role, index)
            
        return jsonFactory.toJson(lobbies[lobbyId], playerId=playerId, currentPlayer=currentPlayer), 201