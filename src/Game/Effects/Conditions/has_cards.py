from Game.Sources.source_factory import SourceFactory

class HasCards:
    """ Represents a condition where a source must have cards """
    
    def __init__(self, sourceType, filter=None):
        """ Initialize the COndition with the Source to check that has cards """
        self.sourceType = sourceType
        self.filter = filter
        
    def evaluate(self, game, event=None):
        """ Evaluate the condition """
        cards = SourceFactory.getSource(self.sourceType, game, event=event)
        if filter is not None:
            cards = self.filter.evaluate(game)
        return len(cards) > 0
        