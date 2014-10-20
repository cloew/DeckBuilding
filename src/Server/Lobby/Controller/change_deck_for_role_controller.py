from Server.Lobby.lobbies import lobbies
from kao_flask.controllers.json_controller import JSONController

class ChangeDeckForRoleController(JSONController):
    """ Controller to handle changing the Deck for a particular role via JSON """
    
    def performWithJSON(self, lobbyId, playerId):
        lobby = lobbies[lobbyId]
        player = lobby.players[playerId]
        lobby.lobby.gameMode.setDeckForRole(self.json['role'], self.json['index'])
        return lobbies[lobbyId].toJSONForPlayer(playerId), 201