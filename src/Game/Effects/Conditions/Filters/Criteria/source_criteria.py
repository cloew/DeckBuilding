from Game.Effects.Conditions.Filters.Operations.operations import operations

class SourceCriteria:
    """ Represents a Criteria based on values from a source """
    
    def __init__(self, field, sourceType):
        """ Initialize the Fixed Criteria """
        self.field = field
        self.sourceType = sourceType
        self.operation = operations["IN"]
        
    def compare(self, card, context):
        """ Compare the card with the Matching Condition """
        source = context.loadSource(self.sourceType)
        value = getattr(card, self.field)
        return self.operation(value, [getattr(sourceCard, self.field) for sourceCard in source])