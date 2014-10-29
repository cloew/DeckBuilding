from Game.Commands.Responses.defend import Defend

from Server.Game.Controller.game_command_controller import GameCommandController

class DefendController(GameCommandController):
    """ Controller to defend """
        
    def buildCommand(self, player, game, json):
        """ Build the Command to try and perform """
        defending = self.json['defending']
        cardIndex = self.json['index']
        
        card = None
        if defending and game.currentTurn.request is not None and cardIndex < len(game.currentTurn.request.defenses):
            card = game.currentTurn.request.defenses[cardIndex]
            command = Defend(card, game.currentTurn)
        return command