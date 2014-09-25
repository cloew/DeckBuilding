from Game.Effects.Conditions.Filters.comparison_filter import ComparisonFilter

class Matching:
    """ Represents a condition where a field must match a value """
    
    def __init__(self, sourceType, criteria, number=None):
        """ Initialize the Matching Condition with the field to use and the values it can match """
        self.filter = ComparisonFilter(sourceType, criteria)
        
        if number is None:
            number = 1
        self.number = number
        
    def evaluate(self, args):
        """ Evaluate the condition """
        return len(self.filter.evaluate(args)) >= self.number
        