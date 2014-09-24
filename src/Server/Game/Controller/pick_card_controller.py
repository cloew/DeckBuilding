from Game.Commands.Responses.pick_card import PickCard
from Server.Game.games import games

from kao_flask.controllers.json_controller import JSONController

class PickCardController(JSONController):
    """ Controller to pick a card """
    
    def performWithJSON(self, gameId, playerId):
        game = games[gameId]
        cardIndices = self.json['indices']
        cards = [game.game.currentTurn.request.cards[cardIndex] for cardIndex in cardIndices]
        
        PickCard(cards, game.game.currentTurn).perform()
        return game.toJSONForPlayer(playerId)