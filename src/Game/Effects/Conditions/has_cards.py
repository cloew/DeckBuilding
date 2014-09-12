from Game.Sources.source_factory import SourceFactory

class HasCards:
    """ Represents a condition where a source must have cards """
    
    def __init__(self, sourceType):
        """ Initialize the COndition with the Source to check that has cards """
        self.sourceType = sourceType
        
    def evaluate(self, game, event=None):
        """ Evaluate the condition """
        return len(SourceFactory.getSource(self.sourceType, game, event=event)) > 0
        