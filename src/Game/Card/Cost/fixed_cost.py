
class FixedCost:
    """ Represents a Fixed Cost method for determining the Cost of a Card """
    
    def __init__(self, cost):
        """ Initialize the Fixed Cost """
        self.cost = cost
        
    def calculateCost(self):
        """ Return the cost """
        return self.cost