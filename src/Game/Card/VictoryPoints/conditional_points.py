
class ConditionalPoints:
    """ Represents a VP based on a condition """
    
    def __init__(self, condition, vpCalculator, otherwise):
        """ Initialize the points to provide """
        self.condition = condition
        self.vpCalculator = vpCalculator
        self.otherwise = otherwise
        
    def calculatePoints(self, context):
        """ Return the number of Points """
        points = 0
        if self.condition.evaluate(context):
            points = self.vpCalculator.calculatePoints(context)
        else:
            points = self.otherwise.calculatePoints(context)
        return points