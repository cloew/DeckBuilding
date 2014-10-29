from Server.Game.games import games

from kao_flask.controllers.json_controller import JSONController

class GameCommandController(JSONController):
    """ Controller to perform a game command """
    
    def performWithJSON(self, gameId, playerId):
        game = games[gameId]
        player = game.players[playerId]
        
        command = self.buildCommand(player, game.game, self.json)
        
        if command is not None and command.canPerform(player, game.game):
            game.game.currentTurn.perform(command)
        
        return game.toJSONForPlayer(playerId)
        
    def buildCommand(self, player, game, json):
        """ MEthod to return the command to be performed, if it cannot be constructed return None """