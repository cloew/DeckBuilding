from Game.Commands.play_card import PlayCard
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
            card = game.game.lineUp[cardIndex]
        
        BuyCard(card, game.game.currentTurn, source).perform()
        return GameWrapper(id=gameId).toJSON()