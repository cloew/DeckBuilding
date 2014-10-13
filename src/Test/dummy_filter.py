
class DummyFilter:
    """ Represents a dummy filter """
    
    def __init__(self, numberOfResults):
        """ Initialize the Filter with the number of results it should return """
        self.numberOfResults = numberOfResults
        
    def evaluate(self, context):
        """ Return the results of the filter """
        return [None for i in range(self.numberOfResults)]