from Game.Commands.command import Command

from Game.Commands.Requirements.indices_in_list import IndicesInList
from Game.Commands.Requirements.request_target import RequestTarget

class PickCard(Command):
    """ Represents a Command to pick a card """
    
    def __init__(self, indices, cards, owner):
        """ Initialize the Pick Card Command """
        self.owner = owner
        self.cardsFinder = IndicesInList(indices, cards)
        Command.__init__(self, [RequestTarget(), self.cardsFinder])
        
    def perform(self):
        """ Perform the command """
        self.owner.continueCommand(self.cardsFinder.chosen)