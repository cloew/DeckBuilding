from command import Command

from Game.Commands.Requirements.card_in_zone import CardInZone
from Game.Commands.Requirements.current_player import CurrentPlayer
from Game.Commands.Requirements.enough_power import EnoughPower
from Game.Commands.Requirements.no_request import NoRequest

from Game.Effects.effect_runner import PerformEffect
from Game.Effects.gain_card import GainCard
from Game.Effects.game_contexts import PlayerContext
from Game.Events.cards_event import CardsEvent
from Game.Notifications.notification_types import BOUGHT_CARD
from Game.Zones.zone_types import EVENT

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
        event = CardsEvent([self.card], zone, context)
        
        self.owner.spendPower(self.card.calculateCost())
        coroutine = PerformEffect(GainCard(EVENT, notificationType=BOUGHT_CARD), event.context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)