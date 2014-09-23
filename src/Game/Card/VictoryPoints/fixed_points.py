
class FixedPoints:
    """ Represents a card that provides a fixed number of victory points """
    
    def __init__(self, points):
        """ Initialize the points to provide """
        self.points = points
        
    def calculatePoints(self):
        """ Return the number of Points """
        return self.points