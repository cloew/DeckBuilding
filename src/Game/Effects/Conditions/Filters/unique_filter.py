
class UniqueFilter:
    """ Represents a filter that returns only unique values """
    
    def __init__(self, field, zoneType):
        """ Initialize the filter """
        self.field = field
        self.zoneType = zoneType
    
    def evaluate(self, context):
        """ Evaluate the condition """
        zone = context.loadZone(self.zoneType)
        
        cards = []
        valueSet = set()
        
        for card in zone:
            value = getattr(card, self.field)
            if value not in valueSet and value is not None:
                cards.append(card)
                valueSet.add(value)
        
        return cards