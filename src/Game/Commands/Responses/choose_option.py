from Game.Commands.command import Command

from Game.Commands.Requirements.request_target import RequestTarget
from Game.Commands.Requirements.index_in_list import IndexInList

class ChooseOption(Command):
    """ Represents a Command to choose an option """
    
    def __init__(self, index, owner):
        """ Initialize the Choose Option Command """
        self.owner = owner
        self.optionFinder = IndexInList(index, self.owner.request.options)
        Command.__init__(self, [RequestTarget(), self.optionFinder])
        
    def perform(self):
        """ Perform the command """
        self.owner.continueCommand(self.optionFinder.chosen)