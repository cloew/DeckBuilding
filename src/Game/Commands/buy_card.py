from command import Command

from Game.Commands.Requirements.current_player import CurrentPlayer
from Game.Commands.Requirements.enough_power import EnoughPower
from Game.Commands.Requirements.index_in_source import IndexInSource
from Game.Commands.Requirements.no_request import NoRequest

from Game.Effects.game_contexts import PlayerContext
from Game.Sources.source_types import DISCARD_PILE

class BuyCard(Command):
    """ Represents a command to buy a card """
    
    def __init__(self, index, sourceType, owner):
        """ Initialize the Buy Card Command """
        self.owner = owner
        self.cardFinder = IndexInSource(index, sourceType)
        Command.__init__(self, [CurrentPlayer(), NoRequest(), self.cardFinder, EnoughPower(self.cardFinder)])
        
    def perform(self):
        """ Perform the command """
        card = self.cardFinder.card
        source = self.cardFinder.source
        context = PlayerContext(self.owner.game, card)
        
        self.owner.spendPower(card.calculateCost())
        coroutine = self.owner.gainCard(card, source, toSource=context.loadSource(DISCARD_PILE))
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)