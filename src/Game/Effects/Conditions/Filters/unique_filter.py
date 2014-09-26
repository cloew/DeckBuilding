from Game.Sources.source_factory import SourceFactory

class UniqueFilter:
    """ Represents a filter that returns only unique values """
    
    def __init__(self, field, sourceType):
        """ Initialize the filter """
        self.field = field
        self.sourceType = sourceType
    
    def evaluate(self, args):
        """ Evaluate the condition """
        source = SourceFactory.getSourceForEffect(self.sourceType, args)
        
        cards = []
        valueSet = set()
        
        for card in source:
            value = getattr(card, self.field)
            if value not in valueSet and value is not None:
                cards.append(card)
                valueSet.add(value)
        
        return cards