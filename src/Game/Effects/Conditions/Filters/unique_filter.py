from Game.Sources.source_factory import SourceFactory

class UniqueFilter:
    """ Represents a filter that returns only unique values """
    
    def __init__(self, field, sourceType):
        """ Initialize the filter """
        self.field = field
        self.sourceType = sourceType
    
    def evaluate(self, game, event=None):
        """ Evaluate the condition """
        source = SourceFactory.getSource(self.sourceType, game, event=event)
        
        cards = []
        valueSet = set()
        
        for card in source:
            value = getattr(card, self.field)
            if value not in valueSet:
                cards.append(card)
                valueSet.add(value)
        
        return cards