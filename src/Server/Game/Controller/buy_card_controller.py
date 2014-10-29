from Game.Commands.buy_card import BuyCard
from Game.Sources.source_factory import SourceFactory

from Server.Game.Controller.game_command_controller import GameCommandController

class BuyCardController(GameCommandController):
    """ Controller to buy a card """
        
    def buildCommand(self, player, game, json):
        """ Build the Command to try and perform """
        cardIndex = self.json['index']
        sourceType = self.json['source']
        
        command = None
        source = SourceFactory.getSource(sourceType, game)
        
        if cardIndex < len(source):
            card = source[cardIndex]
            command = BuyCard(card, game.currentTurn, source)
        
        return command