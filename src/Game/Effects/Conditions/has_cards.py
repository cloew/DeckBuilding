from Game.Sources.source_factory import SourceFactory

class HasCards:
    """ Represents a condition where a source must have cards """
    
    def __init__(self, sourceType, filter=None):
        """ Initialize the COndition with the Source to check that has cards """
        self.sourceType = sourceType
        self.filter = filter
        
    def evaluate(self, args):
        """ Evaluate the condition """
        source = SourceFactory.getSourceForEffect(self.sourceType, args)
        length = 0
        if self.filter is not None:
            length = len(self.filter.evaluate(args))
        else:
            length = source.availableLength()
        return length > 0
        