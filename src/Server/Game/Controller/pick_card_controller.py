from Game.Commands.Responses.pick_card import PickCard

from Server.Game.Controller.game_response_controller import GameResponseController

class PickCardController(GameResponseController):
    """ Controller to pick a card """
        
    def buildCommand(self, player, game, json):
        """ Build the Command to try and perform """
        cardIndices = self.json['indices']
        
        card = None
        if game.currentTurn.request is not None:
            cards = [game.currentTurn.request.cards[cardIndex] for cardIndex in cardIndices if cardIndex < len(game.currentTurn.request.cards)]
            command = PickCard(cards, game.currentTurn)
        return command