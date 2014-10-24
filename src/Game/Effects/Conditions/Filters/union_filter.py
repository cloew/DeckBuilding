
class UnionFilter:
    """ Represents a filter that returns all the values returned from other filters """
    
    def __init__(self, filters):
        """ Initialize the filter """
        self.filters = filters
    
    def evaluate(self, context):
        """ Evaluate the condition """
        cards = []
        return [cards.append(card) for filter in self.filters for card in filter.evaluate(context)]