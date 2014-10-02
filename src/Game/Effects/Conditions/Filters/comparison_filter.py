from Game.Effects.Conditions.Filters.Operations.operations import operations

class ComparisonFilter:
    """ Represents a filter that returns all the cards from a source that pass some comparison """
    
    def __init__(self, sourceType, criteria):
        """ Initialize the filter """
        self.sourceType = sourceType
        self.criteria = criteria
        
    def evaluate(self, context):
        """ Evaluate the condition """
        source = context.loadSource(self.sourceType)
        return [card for card in source if self.criteria.compare(card, context)]