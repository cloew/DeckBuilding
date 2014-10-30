from index_in_list import IndexInList
from Game.Sources.source_factory import SourceFactory

class IndexInSource:
    """ Represents a command requirement that can only be run if the index exists in the source """
    
    def __init__(self, index, sourceType):
        """ Initialize the requirement with the index and source type to check """
        self.index = index
        self.sourceType = sourceType
        
        self.card = None
        self.source = None
    
    def passed(self, player, game):
        """ Return if the requirement passes """
        self.source = self.getSource(player, game)
        indexInListRequirement = IndexInList(self.index, self.source)
        
        passed = indexInListRequirement.passed(player, game)
        self.card = indexInListRequirement.chosen
        
        return passed
        
    def getSource(self, player, game):
        """ Return the source to check """
        return SourceFactory.getSource(self.sourceType, game, player=player)