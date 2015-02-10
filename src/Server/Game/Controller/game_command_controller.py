from Server.helpers.json_factory import jsonFactory
from Server.Game.games import games, gameToPlayers

from kao_flask.controllers.json_controller import JSONController

class GameCommandController(JSONController):
    """ Controller to perform a game command """
    
    def performWithJSON(self, gameId, playerId, json=None):
        game = games[gameId]
        player = gameToPlayers[gameId][playerId]
        
        command = self.buildCommand(player, game, json)
        
        if command is not None and command.canPerform(player, game):
            self.performCommand(game, command)
        return {'game':jsonFactory.toJson(game, gameId=gameId, playerId=playerId, currentPlayer=player)}
        
    def performCommand(self, game, command):
        """ Perform the given command """
        game.currentTurn.perform(command)
        
    def buildCommand(self, player, game, json):
        """ Method to return the command to be performed, if it cannot be constructed return None """