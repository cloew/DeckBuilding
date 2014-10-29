from Game.Commands.command import Command

from Game.Commands.Requirements.request_target import RequestTarget

class PickCard(Command):
    """ Represents a Command to pick a card """
    
    def __init__(self, cards, owner):
        """ Initialize the Pick Card Command """
        self.cards = cards
        self.owner = owner
        Command.__init__(self, [RequestTarget()])
        
    def perform(self):
        """ Perform the command """
        self.owner.continueCommand(self.cards)