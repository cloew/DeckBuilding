from Game.Commands.command import Command

from Game.Commands.Requirements.request_target import RequestTarget

class Defend(Command):
    """ Represents a Command to defend """
    
    def __init__(self, card, owner):
        """ Initialize the Defend Command """
        self.card = card
        self.owner = owner
        Command.__init__(self, [RequestTarget()])
        
    def perform(self):
        """ Perform the command """
        self.owner.continueCommand(self.card)