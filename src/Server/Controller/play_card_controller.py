from Game.Commands.play_card import PlayCard
from Server.Game.game_wrapper import GameWrapper

from kao_flask.controllers.json_controller import JSONController

class PlayCardController(JSONController):
    """ Controller to play a card """
    
    def performWithJSON(self, gameId):
        game = GameWrapper(id=gameId)
        cardIndex = self.json['index']
        card = game.game.currentTurn.player.hand[cardIndex]
        game.game.currentTurn.perform(PlayCard(card, game.game.currentTurn))
        return game.toJSON()