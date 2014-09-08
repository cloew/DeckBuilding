from Game.Sources.source_factory import SourceFactory
from Game.Effects.Conditions.Operations.operations import operations

class Matching:
    """ Represents a condition where a filed must match a value """
    
    def __init__(self, field, values, sourceType):
        """ Initialize the Matching Condition with the field to use and the values it can match """
        self.field = field
        self.values = values
        self.sourceType = sourceType
        self.operation = operations["IN"]
        
    def evaluate(self, game, event=None):
        """ Evaluate the condition """
        matches = False
        source = SourceFactory.getSource(self.sourceType, game, event=event)
        return any([self.compare(card) for card in source])
        
    def compare(self, card):
        """ Compare the card with the Matching Condition """
        value = getattr(card, self.field)
        return self.operation.compare(value, self.values)
        