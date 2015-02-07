from Game.Commands.buy_card import BuyCard

from Server.Game.Controller.game_and_card_command_controller import GameAndCardCommandController

class BuyCardController(GameAndCardCommandController):
    """ Controller to buy a card """
        
    def buildCommand(self, player, game, card, json):
        """ Build the Command to try and perform """
        zoneType = json['zone']
        return BuyCard(card, zoneType, game.currentTurn)