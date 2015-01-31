from Server.Game.games import games

from kao_flask.controllers.json_controller import JSONController

class GameCommandController(JSONController):
    """ Controller to perform a game command """
    
    def performWithJSON(self, gameId, playerId, json=None):
        game = games[gameId]
        player = game.players[playerId]
        
        command = self.buildCommand(player, game.game, json)
        
        if command is not None and command.canPerform(player, game.game):
            self.performCommand(game.game, command)
        return game.toJSONForPlayer(playerId)
        
    def performCommand(self, game, command):
        """ Perform the given command """
        game.currentTurn.perform(command)
        
    def buildCommand(self, player, game, json):
        """ Method to return the command to be performed, if it cannot be constructed return None """