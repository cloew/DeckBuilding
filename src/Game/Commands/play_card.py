from command import Command

from Game.Commands.Requirements.current_player import CurrentPlayer
from Game.Commands.Requirements.index_in_zone import IndexInZone
from Game.Commands.Requirements.no_request import NoRequest
from Game.Zones.zone_types import HAND

class PlayCard(Command):
    """ Represents a Command to play a card """
    
    def __init__(self, index, owner):
        """ Initialize the Play Card Command """
        self.owner = owner
        self.cardFinder = IndexInZone(index, HAND)
        Command.__init__(self, [CurrentPlayer(), NoRequest(), self.cardFinder])
        
    def perform(self):
        """ Perform the command """
        coroutine = self.owner.playCardFromHand(self.cardFinder.card)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)