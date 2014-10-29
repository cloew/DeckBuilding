
class Command:
    """ Represents a game command """
    
    def __init__(self, requirements):
        """ Initialize the Command with the requirements that must be met for it to run """
        self.requirements = requirements
    
    def canPerform(self, player, game):
        """ Returns if the command can be performed by the given player for the current game state """
        return all([requirement.passed(player, game) for requirement in self.requirements])