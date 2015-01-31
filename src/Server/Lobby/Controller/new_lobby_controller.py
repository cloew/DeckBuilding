from Server.Lobby.lobbies import StartNewLobby, lobbies
from kao_flask.controllers.json_controller import JSONController

class NewLobbyController(JSONController):
    """ Controller to handle creating a new Game Lobby via JSON """
    
    def performWithJSON(self, json=None):
        lobby = StartNewLobby()
        playerId = lobby.addPlayer()
        return {'playerId':playerId, 'lobbyId':lobby.id}, 201