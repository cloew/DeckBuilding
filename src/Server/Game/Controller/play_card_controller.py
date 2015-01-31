from Game.Commands.play_card import PlayCard

from Server.Game.Controller.game_command_controller import GameCommandController

class PlayCardController(GameCommandController):
    """ Controller to play a card """
        
    def buildCommand(self, player, game, json):
        """ Build the Command to try and perform """
        cardIndex = json['index']
        return PlayCard(cardIndex, game.currentTurn)