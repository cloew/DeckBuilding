from Game.Commands.buy_card import BuyCard
from Game.Sources.source_factory import SourceFactory
from Server.Game.games import games

from kao_flask.controllers.json_controller import JSONController

class BuyCardController(JSONController):
    """ Controller to buy a card """
    
    def performWithJSON(self, gameId):
        game = games[gameId]
        cardIndex = self.json['index']
        sourceType = self.json['source']
        
        card = None
        source = SourceFactory.getSource(sourceType, game.game)
        card = source[cardIndex]
        
        game.game.currentTurn.perform(BuyCard(card, game.game.currentTurn, source))
        return game.toJSON()