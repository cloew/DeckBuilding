from command import Command

from Game.Commands.Requirements.card_in_zone import CardInZone
from Game.Commands.Requirements.current_player import CurrentPlayer
from Game.Commands.Requirements.enough_power import EnoughPower
from Game.Commands.Requirements.no_request import NoRequest

from Game.Effects.game_contexts import PlayerContext
from Game.Zones.zone_types import DISCARD_PILE

class BuyCard(Command):
    """ Represents a command to buy a card """
    
    def __init__(self, card, zoneType, owner):
        """ Initialize the Buy Card Command """
        self.owner = owner
        self.card = card
        self.zoneType = zoneType
        Command.__init__(self, [CurrentPlayer(), NoRequest(), CardInZone(card, zoneType), EnoughPower(self.card)])
        
    def perform(self):
        """ Perform the command """
        context = PlayerContext(self.owner.game, self.card)
        zone = context.loadZone(self.zoneType)
        
        self.owner.spendPower(self.card.calculateCost())
        coroutine = self.owner.gainCard(self.card, zone, toZone=context.loadZone(DISCARD_PILE))
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)