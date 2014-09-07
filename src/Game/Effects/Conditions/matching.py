
class Matching:
    """ Represents a condition where a filed must match a value """
    
    def __init__(self, field, values, source):
        """ Initialize the Matching Condition with the field to use and the values it can match """
        self.field = field
        self.values = values
        
    def evaluate(self):
        """ Evaluate the condition """
        matches = False
        for card in source:
            value = getattr(card, self.field)
            matches = value in self.values
            if matches is True:
                break
        return matches