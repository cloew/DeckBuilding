from Game.Commands.activate_card import ActivateCard

from Server.Game.Controller.game_command_controller import GameCommandController

class ActivateCardController(GameCommandController):
    """ Controller to activate a card """
        
    def buildCommand(self, player, game, json):
        """ Build the Command to try and perform """
        cardIndex = json['index']
        sourceType = json['source']
        return ActivateCard(cardIndex, sourceType, game.currentTurn)