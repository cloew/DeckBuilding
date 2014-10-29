from command import Command
from Game.Commands.Requirements.current_player import CurrentPlayer

from Game.Effects.game_contexts import PlayerContext
from Game.Sources.source_types import DISCARD_PILE

class BuyCard(Command):
    """ Represents a command to buy a card """
    
    def __init__(self, card, owner, source):
        """ Initialize the Buy Card Command """
        self.card = card
        self.owner = owner
        self.source = source
        Command.__init__(self, [CurrentPlayer()])
        
    def perform(self):
        """ Perform the command """
        context = PlayerContext(self.owner.game, self.card)
        self.owner.spendPower(self.card.calculateCost())
        coroutine = self.owner.gainCard(self.card, self.source, toSource=context.loadSource(DISCARD_PILE))
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)