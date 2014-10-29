from Game.Commands.command import Command

from Game.Commands.Requirements.request_target import RequestTarget

class ChooseOption(Command):
    """ Represents a Command to choose an option """
    
    def __init__(self, option, owner):
        """ Initialize the Choose Option Command """
        self.option = option
        self.owner = owner
        Command.__init__(self, [RequestTarget()])
        
    def perform(self):
        """ Perform the command """
        self.owner.continueCommand(self.option)