from Server.Lobby.lobbies import lobbies
from kao_flask.controllers.json_controller import JSONController

class ChangeNameController(JSONController):
    """ Controller to handle changing a player's name via JSON """
    
    def performWithJSON(self, lobbyId, playerId, json=None):
        lobby = lobbies[lobbyId]
        player = lobby.players[playerId]
        player.setName(json['name'])
        return lobbies[lobbyId].toJSONForPlayer(playerId), 201