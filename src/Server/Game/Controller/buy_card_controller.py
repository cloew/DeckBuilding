from Game.Commands.buy_card import BuyCard
from Game.Sources.source_factory import SourceFactory
from Server.Game.games import games

from kao_flask.controllers.json_controller import JSONController

class BuyCardController(JSONController):
    """ Controller to buy a card """
    
    def performWithJSON(self, gameId, playerId):
        game = games[gameId]
        player = game.players[playerId]
        
        command = self.buildCommand(player, game.game, self.json)
        
        if command.canPerform(player, game.game):
            game.game.currentTurn.perform(command)
        
        return game.toJSONForPlayer(playerId)
        
    def buildCommand(self, player, game, json):
        """ Build the Command to try and perform """
        cardIndex = self.json['index']
        sourceType = self.json['source']
        
        card = None
        source = SourceFactory.getSource(sourceType, game)
        card = source[cardIndex]
        
        return BuyCard(card, game.currentTurn, source)