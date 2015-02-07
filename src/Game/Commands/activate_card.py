from command import Command

from Game.Commands.Requirements.card_in_zone import CardInZone
from Game.Commands.Requirements.current_player import CurrentPlayer
from Game.Commands.Requirements.index_in_zone import IndexInZone
from Game.Commands.Requirements.no_request import NoRequest

from Game.Effects.game_contexts import PlayerContext

class ActivateCard(Command):
    """ Represents a command to activate a card """
    
    def __init__(self, card, zoneType, owner):
        """ Initialize the Activate Card Command """
        self.owner = owner
        self.card = card
        Command.__init__(self, [CurrentPlayer(), NoRequest(), CardInZone(card, zoneType)])
        
    def perform(self):
        """ Perform the command """
        context = PlayerContext(self.owner.game, self.card)
        coroutine = self.owner.activatableEffects[self.card][0].activate(context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)