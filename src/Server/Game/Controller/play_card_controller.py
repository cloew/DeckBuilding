from Game.Commands.play_card import PlayCard

from Server.Game.Controller.game_and_card_command_controller import GameAndCardCommandController

class PlayCardController(GameAndCardCommandController):
    """ Controller to play a card """
        
    def buildCommand(self, player, game, card, json):
        """ Build the Command to try and perform """
        return PlayCard(card, game.currentTurn)