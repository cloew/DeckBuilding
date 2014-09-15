from Game.Commands.Responses.pick_card import PickCard
from Server.Game.game_wrapper import GameWrapper

from kao_flask.controllers.json_controller import JSONController

class PickCardController(JSONController):
    """ Controller to pick a card """
    
    def performWithJSON(self, gameId):
        game = GameWrapper(id=gameId)
        cardIndex = self.json['index']
        card = game.game.currentTurn.request.cards[cardIndex]
        PickCard(card, game.game.currentTurn).perform()
        return game.toJSON()