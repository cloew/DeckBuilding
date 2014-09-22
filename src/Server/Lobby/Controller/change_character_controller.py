from Server.Lobby.lobbies import lobbies
from kao_flask.controllers.json_controller import JSONController

class ChangeCharacterController(JSONController):
    """ Controller to handle creating a new Game Lobby via JSON """
    
    def performWithJSON(self, lobbyId, playerId):
        lobby = lobbies[lobbyId]
        player = lobby.players[playerId]
        player.character = self.json['character']
        return lobbies[lobbyId].toJSONForPlayer(playerId), 201