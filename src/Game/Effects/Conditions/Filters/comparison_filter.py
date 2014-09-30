from Game.Effects.Conditions.Filters.Operations.operations import operations
from Game.Sources.source_factory import SourceFactory

class ComparisonFilter:
    """ Represents a filter that returns all the cards from a source that pass some comparison """
    
    def __init__(self, sourceType, criteria):
        """ Initialize the filter """
        self.sourceType = sourceType
        self.criteria = criteria
        
    def evaluate(self, args):
        """ Evaluate the condition """
        print "Source Type:", self.sourceType
        source = SourceFactory.getSourceForEffect(self.sourceType, args)
        print "Source:", source
        return [card for card in source if self.criteria.compare(card, args)]