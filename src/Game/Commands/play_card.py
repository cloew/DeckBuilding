from command import Command

from Game.Commands.Requirements.current_player import CurrentPlayer
from Game.Commands.Requirements.no_request import NoRequest

class PlayCard(Command):
    """ Represents a Command to play a card """
    
    def __init__(self, card, owner):
        """ Initialize the Play Card Command """
        self.card = card
        self.owner = owner
        Command.__init__(self, [CurrentPlayer(), NoRequest()])
        
    def perform(self):
        """ Perform the command """
        coroutine = self.owner.playCardFromHand(self.card)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)