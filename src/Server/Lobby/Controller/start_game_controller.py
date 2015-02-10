from Server.Lobby.lobbies import lobbies, StartGameFor
from kao_flask.controllers.json_controller import JSONController

class StartGameController(JSONController):
    """ Controller to handle creating a new Game Lobby via JSON """
    
    def performWithJSON(self, lobbyId, json=None):
        gameId = StartGameFor(lobbyId)
        return {'gameId':gameId}, 201