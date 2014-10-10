from Game.Effects.Conditions.Filters.comparison_filter import ComparisonFilter

class Matching:
    """ Represents a condition where a field must match a value """
    
    def __init__(self, sourceType, criteria=None, number=None):
        """ Initialize the Matching Condition with the field to use and the values it can match """
        self.sourceType = sourceType
        self.filter = None
        if criteria is not None:
            self.filter = ComparisonFilter(sourceType, criteria)
        
        if number is None:
            number = 1
        self.number = number
        
    def evaluate(self, context):
        """ Evaluate the condition """
        source = context.loadSource(self.sourceType)
        length = 0
        if self.filter is not None:
            length = len(self.filter.evaluate(context))
        else:
            length = source.availableLength()
        return length >= self.number
        