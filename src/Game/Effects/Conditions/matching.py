from Game.Sources.source_factory import SourceFactory

class Matching:
    """ Represents a condition where a filed must match a value """
    
    def __init__(self, field, values, sourceType):
        """ Initialize the Matching Condition with the field to use and the values it can match """
        self.field = field
        self.values = values
        self.sourceType = sourceType
        
    def evaluate(self, game, event=None):
        """ Evaluate the condition """
        matches = False
        source = SourceFactory.getSource(self.sourceType, game, event=event)
        
        for card in source:
            value = getattr(card, self.field)
            matches = value in self.values
            
            if matches is True:
                break
                
        return matches