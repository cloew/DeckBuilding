from Game.Commands.Responses.defend import Defend

from Server.Game.Controller.game_response_controller import GameResponseController

class DefendController(GameResponseController):
    """ Controller to defend """
        
    def buildCommand(self, player, game, json):
        """ Build the Command to try and perform """
        defending = json['defending']
        cardIndex = None
        if 'index' in json:
            cardIndex = json['index']
        
        return Defend(defending, cardIndex, game.currentTurn)