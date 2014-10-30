from Game.Sources.source_factory import SourceFactory

class IndexInList:
    """ Represents a command requirement that can only be run if the index exists in the list """
    
    def __init__(self, index, possibilities):
        """ Initialize the requirement with the index and list to check """
        self.index = index
        self.possibilities = possibilities
        
        self.chosen = None
    
    def passed(self, player, game):
        """ Return if the requirement passes """
        passed = self.index < len(self.possibilities)
        
        if passed:
            self.chosen = self.possibilities[self.index]
        return passed