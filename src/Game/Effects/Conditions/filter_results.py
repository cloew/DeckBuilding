
class FilterResults:
    """ Represents a condition where a certain number of values froma filter must exist """
    
    def __init__(self, zoneType, filter=None, number=None):
        """ Initialize the Filter Results Condition with the filter to use """
        self.zoneType = zoneType
        self.filter = filter
        
        if number is None:
            number = 1
        self.number = number
        
    def evaluate(self, context):
        """ Evaluate the condition """
        zone = context.loadZone(self.zoneType)
        length = 0
        if self.filter is not None:
            length = len(self.filter.evaluate(context))
        else:
            length = zone.availableLength()
        return length >= self.number
        