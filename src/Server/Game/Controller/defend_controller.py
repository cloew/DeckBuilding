from Game.Commands.Responses.defend import Defend

from Server.Game.Controller.game_command_controller import GameCommandController

class DefendController(GameCommandController):
    """ Controller to defend """
        
    def buildCommand(self, player, game, json):
        """ Build the Command to try and perform """
        defending = self.json['defending']
        
        command = None
        if game.currentTurn.request is not None:
            if defending:
                cardIndex = self.json['index']
                if cardIndex < len(game.currentTurn.request.defenses):
                    card = game.currentTurn.request.defenses[cardIndex]
                    command = Defend(card, game.currentTurn)
            else:
                command = Defend(None, game.currentTurn)
        return command