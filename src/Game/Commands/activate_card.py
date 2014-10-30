from command import Command

from Game.Commands.Requirements.current_player import CurrentPlayer
from Game.Commands.Requirements.index_in_source import IndexInSource
from Game.Commands.Requirements.no_request import NoRequest

from Game.Effects.game_contexts import PlayerContext

class ActivateCard(Command):
    """ Represents a command to activate a card """
    
    def __init__(self, index, sourceType, owner):
        """ Initialize the Activate Card Command """
        self.owner = owner
        self.cardFinder = IndexInSource(index, sourceType)
        Command.__init__(self, [CurrentPlayer(), NoRequest(), self.cardFinder])
        
    def perform(self):
        """ Perform the command """
        card = self.cardFinder.card
        context = PlayerContext(self.owner.game, card)
        coroutine = self.owner.activatableEffects[card][0].activate(context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)