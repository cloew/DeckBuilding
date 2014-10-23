
class FilterResults:
    """ Represents a condition where a certain number of values froma filter must exist """
    
    def __init__(self, sourceType, filter=None, number=None):
        """ Initialize the Filter Results Condition with the filter to use """
        self.sourceType = sourceType
        self.filter = filter
        
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
        