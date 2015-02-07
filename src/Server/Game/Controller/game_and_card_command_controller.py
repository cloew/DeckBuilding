from Server.Game.games import games

from kao_flask.controllers.json_controller import JSONController

class GameAndCardCommandController(JSONController):
    """ Controller to perform a game command with a card """
    
    def performWithJSON(self, gameId, playerId, cardId, json=None):
        game = games[gameId]
        player = game.players[playerId]
        print game.game.cardIdManager.idToCard
        card = game.game.getCardFromId(cardId)
        
        command = self.buildCommand(player, game.game, card, json)
        
        if command is not None and command.canPerform(player, game.game):
            self.performCommand(game.game, command)
        return game.toJSONForPlayer(playerId)
        
    def performCommand(self, game, command):
        """ Perform the given command """
        game.currentTurn.perform(command)
        
    def buildCommand(self, player, game, card, json):
        """ Method to return the command to be performed, if it cannot be constructed return None """