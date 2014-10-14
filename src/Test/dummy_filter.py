
class DummyFilter:
    """ Represents a dummy filter """
    
    def __init__(self, numberOfResults=None, results=[]):
        """ Initialize the Filter with the number of results it should return """
        if results == [] and numberOfResults is not None:
            results = [None for i in range(numberOfResults)]
        self.results = results
        
    def evaluate(self, context):
        """ Return the results of the filter """
        return self.results