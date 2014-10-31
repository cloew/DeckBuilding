from Game.Decks.deck_roles import STARTING
from Server.Lobby.lobbies import lobbies
from kao_flask.controllers.json_controller import JSONController

class ChangeDeckForRoleController(JSONController):
    """ Controller to handle changing the Deck for a particular role via JSON """
    
    def performWithJSON(self, lobbyId, playerId):
        lobby = lobbies[lobbyId]
        player = lobby.players[playerId]
        role = self.json['role']
        index = self.json['index']
        
        if role == STARTING:
            player.setDeck(index)
        else:
            lobby.lobby.gameMode.setDeckForRole(role, index)
            
        return lobbies[lobbyId].toJSONForPlayer(playerId), 201