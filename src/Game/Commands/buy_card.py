from command import Command

from Game.Commands.Requirements.current_player import CurrentPlayer
from Game.Commands.Requirements.enough_power import EnoughPower
from Game.Commands.Requirements.index_in_zone import IndexInZone
from Game.Commands.Requirements.no_request import NoRequest

from Game.Effects.game_contexts import PlayerContext
from Game.Zones.zone_types import DISCARD_PILE

class BuyCard(Command):
    """ Represents a command to buy a card """
    
    def __init__(self, index, zoneType, owner):
        """ Initialize the Buy Card Command """
        self.owner = owner
        self.cardFinder = IndexInZone(index, zoneType)
        Command.__init__(self, [CurrentPlayer(), NoRequest(), self.cardFinder, EnoughPower(self.cardFinder)])
        
    def perform(self):
        """ Perform the command """
        card = self.cardFinder.card
        zone = self.cardFinder.zone
        context = PlayerContext(self.owner.game, card)
        
        self.owner.spendPower(card.calculateCost())
        coroutine = self.owner.gainCard(card, zone, toZone=context.loadZone(DISCARD_PILE))
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)