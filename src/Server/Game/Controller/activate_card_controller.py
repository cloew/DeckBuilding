from Game.Commands.activate_card import ActivateCard

from Server.Game.Controller.game_and_card_command_controller import GameAndCardCommandController

class ActivateCardController(GameAndCardCommandController):
    """ Controller to activate a card """
        
    def buildCommand(self, player, game, card, json):
        """ Build the Command to try and perform """
        zoneType = json['zone']
        return ActivateCard(card, zoneType, game.currentTurn)