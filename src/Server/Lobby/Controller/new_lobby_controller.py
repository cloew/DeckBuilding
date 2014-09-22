from Server.Lobby.lobbies import StartNewLobby
from Server.Lobby.lobby_wrapper import LobbyWrapper
from kao_flask.controllers.json_controller import JSONController

class NewLobbyController(JSONController):
    """ Controller to handle creating a new Game Lobby via JSON """
    
    def performWithJSON(self):
        id = StartNewLobby()
        return LobbyWrapper(id=id).toJSON(), 201