
class UniqueFilter:
    """ Represents a filter that returns only unique values """
    
    def __init__(self, field, sourceType):
        """ Initialize the filter """
        self.field = field
        self.sourceType = sourceType
    
    def evaluate(self, context):
        """ Evaluate the condition """
        source = context.loadSource(self.sourceType)
        
        cards = []
        valueSet = set()
        
        for card in source:
            value = getattr(card, self.field)
            if value not in valueSet and value is not None:
                cards.append(card)
                valueSet.add(value)
        
        return cards