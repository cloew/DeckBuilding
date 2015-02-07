from command import Command

from Game.Commands.Requirements.card_in_zone import CardInZone
from Game.Commands.Requirements.current_player import CurrentPlayer
from Game.Commands.Requirements.no_request import NoRequest
from Game.Zones.zone_types import HAND

class PlayCard(Command):
    """ Represents a Command to play a card """
    
    def __init__(self, card, owner):
        """ Initialize the Play Card Command """
        self.owner = owner
        self.card = card
        Command.__init__(self, [CurrentPlayer(), NoRequest(), CardInZone(card, HAND)])
        
    def perform(self):
        """ Perform the command """
        coroutine = self.owner.playCardFromHand(self.card)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)