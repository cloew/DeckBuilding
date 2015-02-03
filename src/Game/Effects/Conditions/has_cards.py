
class HasCards:
    """ Represents a condition where a zone must have cards """
    
    def __init__(self, zoneType, filter=None):
        """ Initialize the Condition with the Zone to check that has cards """
        self.zoneType = zoneType
        self.filter = filter
        
    def evaluate(self, context):
        """ Evaluate the condition """
        zone = context.loadZone(self.zoneType)
        length = 0
        if self.filter is not None:
            length = len(self.filter.evaluate(context))
        else:
            length = zone.availableLength()
        return length > 0
        