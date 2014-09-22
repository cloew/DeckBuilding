from Game.Commands.Responses.pick_card import PickCard
from Server.Game.games import games

from kao_flask.controllers.json_controller import JSONController

class PickCardController(JSONController):
    """ Controller to pick a card """
    
    def performWithJSON(self, gameId):
        game = games[gameId]
        cardIndex = self.json['index']
        card = game.game.currentTurn.request.cards[cardIndex]
        
        PickCard(card, game.game.currentTurn).perform()
        return game.toJSON()