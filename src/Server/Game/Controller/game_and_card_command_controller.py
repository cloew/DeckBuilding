from Server.helpers.json_factory import jsonFactory
from Server.Game.games import games, gameToPlayers

from kao_flask.controllers.json_controller import JSONController

class GameAndCardCommandController(JSONController):
    """ Controller to perform a game command with a card """
    
    def performWithJSON(self, gameId, playerId, cardId, json=None):
        game = games[gameId]
        player = gameToPlayers[gameId][playerId]
        card = game.getCardFromId(cardId)
        
        command = self.buildCommand(player, game, card, json)
        
        if command is not None and command.canPerform(player, game):
            self.performCommand(game, command)
        return {'game':jsonFactory.toJson(game, gameId=gameId, playerId=playerId, currentPlayer=player)}
        
    def performCommand(self, game, command):
        """ Perform the given command """
        game.currentTurn.perform(command)
        
    def buildCommand(self, player, game, card, json):
        """ Method to return the command to be performed, if it cannot be constructed return None """