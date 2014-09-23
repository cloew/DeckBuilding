from Server.Lobby.lobbies import lobbies
from kao_flask.controllers.json_controller import JSONController

class StartGameController(JSONController):
    """ Controller to handle creating a new Game Lobby via JSON """
    
    def performWithJSON(self, lobbyId):
        lobby = lobbies[lobbyId]
        # del lobbies[lobbyId]
        gameId = lobby.startGame()
        return {'gameId':gameId}, 201