from Server.Lobby.lobbies import lobbies
from kao_flask.controllers.json_controller import JSONController

class JoinLobbyController(JSONController):
    """ Controller to handle creating a new Game Lobby via JSON """
    
    def performWithJSON(self, lobbyId):
        lobby = lobbies[lobbyId]
        playerId = lobby.addPlayer()
        return {'playerId':playerId, 'lobbyId':lobby.id}, 201