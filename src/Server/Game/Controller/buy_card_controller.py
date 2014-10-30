from Game.Commands.buy_card import BuyCard

from Server.Game.Controller.game_command_controller import GameCommandController

class BuyCardController(GameCommandController):
    """ Controller to buy a card """
        
    def buildCommand(self, player, game, json):
        """ Build the Command to try and perform """
        cardIndex = json['index']
        sourceType = json['source']
        return BuyCard(cardIndex, sourceType, game.currentTurn)