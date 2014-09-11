from Game.Commands.buy_card import BuyCard
from Game.Sources.source_factory import SourceFactory
from Server.Game.game_wrapper import GameWrapper

from kao_flask.controllers.json_controller import JSONController

class BuyCardController(JSONController):
    """ Controller to buy a card """
    
    def performWithJSON(self, gameId):
        game = GameWrapper(id=gameId)
        cardIndex = self.json['index']
        sourceType = self.json['source']
        
        card = None
        source = SourceFactory.getSource(sourceType, game.game)
        card = source[cardIndex]
        
        BuyCard(card, game.game.currentTurn, source).perform()
        return game.toJSON()