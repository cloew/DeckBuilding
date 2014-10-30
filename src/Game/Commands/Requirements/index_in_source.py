from Game.Sources.source_factory import SourceFactory

class IndexInSource:
    """ Represents a command requirement that can only be run if the index exists in the source """
    
    def __init__(self, index, sourceType):
        """ Initialize the requirement with the index and source type to check """
        self.index = index
        self.sourceType = sourceType
        self.card = None
    
    def passed(self, player, game):
        """ Return if the requirement passes """
        source = self.getSource(player, game)
        passed = self.index < len(source)
        
        if passed:
            self.card = source[self.index]
        return passed
        
    def getSource(self, player, game):
        """ Return the source to check """
        return SourceFactory.getSource(self.sourceType, game, player=player)