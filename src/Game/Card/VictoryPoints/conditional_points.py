
class ConditionalPoints:
    """ Represents a VP based on a condition """
    
    def __init__(self, condition, vpCalculator, otherwise):
        """ Initialize the points to provide """
        self.condition = condition
        self.vpCalculator = vpCalculator
        self.otherwise = otherwise
        
    def calculatePoints(self, args):
        """ Return the number of Points """
        points = 0
        if self.condtion.evaluate(args):
            points = self.vpCalculator.calculatePoints(args)
        else:
            points = self.otherwise.calculatePoints(args)
        return points