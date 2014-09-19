from Game.Effects.Conditions.Filters.Operations.operations import operations
from Game.Sources.source_factory import SourceFactory

class ComparisonFilter:
    """ Represents a filter that returns all the cards from a source that pass some comparison """
    
    def __init__(self, field, values, sourceType, operation):
        """ Initialize the filter """
        self.field = field
        self.values = values
        self.sourceType = sourceType
        self.operation = operations[operation]
        
    def evaluate(self, game, event=None):
        """ Evaluate the condition """
        source = SourceFactory.getSource(self.sourceType, game, event=event)
        return [card for card in source if self.compare(card)]
        
    def compare(self, card):
        """ Compare the card with the Matching Condition """
        value = getattr(card, self.field)
        return self.operation(value, self.values)