from Server.Game.games import games
from kao_flask.controllers.json_controller import JSONController

class StartGameController(JSONController):
    """ Controller to handle starting a new Game via JSON """
    
    def performWithJSON(self):
        id = StartNewGame()
        return games[id].toJSON(), 201