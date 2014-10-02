
class IntersectionFilter:
    """ Represents a filter that returns the shared values returned between other filters """
    
    def __init__(self, filters):
        """ Initialize the filter """
        self.filters = filters
    
    def evaluate(self, context):
        """ Evaluate the condition """
        cardSets = [set(filter.evaluate(context)) for filter in self.filters]
        
        intersection = cardSets[0]
        for cardSet in cardSets[1:]:
            intersection = intersection & cardSet
            
        return list(intersection)