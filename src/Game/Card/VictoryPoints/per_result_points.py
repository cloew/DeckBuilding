
class PerResultPoints:
    """ Represents a VP based on a condition """
    
    def __init__(self, filter, points=None):
        """ Initialize the filter to get results from """
        self.filter = filter
        if points is None:
            points = 1
        self.points = points
        
    def calculatePoints(self, args):
        """ Return the number of Points """
        return len(self.filter.evaluate(args))*self.points