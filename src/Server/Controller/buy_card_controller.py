from Game.Commands.buy_card import BuyCard
from Server.Game.game_wrapper import GameWrapper

from kao_flask.controllers.json_controller import JSONController

class BuyCardController(JSONController):
    """ Controller to buy a card """
    
    def performWithJSON(self, gameId):
        game = GameWrapper(id=gameId)
        cardIndex = self.json['index']
        source = self.json['source']
        
        card = None
        if source == 'lineUp':
            source = game.game.lineUp
            card = source.cards[cardIndex]
        elif source == 'kick':
            source = game.game.kickDeck
            card = source.peek()
        
        BuyCard(card, game.game.currentTurn, source).perform()
        return game.toJSON()