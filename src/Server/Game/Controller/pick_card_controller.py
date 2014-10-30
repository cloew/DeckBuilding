from Game.Commands.Responses.pick_card import PickCard

from Server.Game.Controller.game_response_controller import GameResponseController

class PickCardController(GameResponseController):
    """ Controller to pick a card """
        
    def buildCommand(self, player, game, json):
        """ Build the Command to try and perform """
        cardIndices = json['indices']
        return PickCard(cardIndices, game.currentTurn.request.cards, game.currentTurn)