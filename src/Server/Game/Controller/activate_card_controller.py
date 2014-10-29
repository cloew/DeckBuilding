from Game.Commands.activate_card import ActivateCard
from Game.Sources.source_factory import SourceFactory
from Server.Game.games import games

from Server.Game.Controller.game_command_controller import GameCommandController

class ActivateCardController(GameCommandController):
    """ Controller to activate a card """
        
    def buildCommand(self, player, game, json):
        """ Build the Command to try and perform """
        cardIndex = self.json['index']
        sourceType = self.json['source']
        
        command = None
        source = SourceFactory.getSource(sourceType, game, player=player)
        
        if cardIndex < len(source):
            card = source[cardIndex]
            command = ActivateCard(card, game.currentTurn)
        
        return command