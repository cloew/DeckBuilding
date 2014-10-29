from Game.Commands.play_card import PlayCard
from Game.Sources.source_factory import SourceFactory
from Game.Sources.source_types import HAND

from Server.Game.Controller.game_command_controller import GameCommandController

class PlayCardController(GameCommandController):
    """ Controller to play a card """
        
    def buildCommand(self, player, game, json):
        """ Build the Command to try and perform """
        cardIndex = self.json['index']
        
        command = None
        source = SourceFactory.getSource(HAND, game, player=player)
        
        if cardIndex < len(source):
            card = source[cardIndex]
            command = PlayCard(card, game.currentTurn)
        return command