from Server.Game.games import StartNewGame
from Server.Game.game_wrapper import GameWrapper
from kao_flask.controllers.json_controller import JSONController

class StartGameController(JSONController):
    """ Controller to handle starting a new Game via JSON """
    
    def performWithJSON(self):
        id = StartNewGame()
        return GameWrapper(id=id).toJSON(), 201