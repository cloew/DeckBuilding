from Game.Commands.command import Command

from Game.Commands.Requirements.index_in_list import IndexInList
from Game.Commands.Requirements.request_target import RequestTarget

class Defend(Command):
    """ Represents a Command to defend """
    
    def __init__(self, defending, index, owner):
        """ Initialize the Defend Command """
        self.owner = owner
        self.cardFinder = IndexInList(index, self.owner.request.defenses)
        
        requirements = [RequestTarget()]
        if defending:
            requirements.append(self.cardFinder)
        Command.__init__(self, requirements)
        
    def perform(self):
        """ Perform the command """
        self.owner.continueCommand(self.cardFinder.chosen)