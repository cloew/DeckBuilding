from Server.game_wrapper import GameWrapper
from kao_flask.controllers.json_controller import JSONController

class GuessController(JSONController):
    """ Controller to allow a player to guess the word for the current Round """
    
    def performWithJSON(self, gameId):
        game = GameWrapper(id=gameId)
        results = game.guess(self.json['guesses'])
        return game.toJSON()