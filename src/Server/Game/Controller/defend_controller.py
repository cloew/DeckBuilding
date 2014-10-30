from Game.Commands.Responses.defend import Defend

from Server.Game.Controller.game_command_controller import GameCommandController

class DefendController(GameCommandController):
    """ Controller to defend """
        
    def buildCommand(self, player, game, json):
        """ Build the Command to try and perform """
        defending = json['defending']
        cardIndex = None
        if 'index' in json:
            cardIndex = json['index']
        
        return Defend(defending, cardIndex, game.currentTurn)