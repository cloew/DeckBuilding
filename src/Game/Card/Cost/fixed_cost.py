
class FixedCost:
    """ Represents a Fixed Cost method for determining the Cost of a Card """
    
    def __init__(self, cost, canBeNegative=False):
        """ Initialize the Fixed Cost """
        self.cost = cost
        self.costModifiers = []
        self.canBeNegative = canBeNegative
        
    def calculateCost(self):
        """ Return the cost """
        currentCost = sum([self.cost] + [costMod.calculateCost() for costMod in self.costModifiers])
        if not self.canBeNegative:
            currentCost = max(currentCost, 0)
        return currentCost
        
    def addCostModifier(self, costMod):
        """ Add the Cost Modifier to the Cost Calcualtor """
        self.costModifiers.append(costMod)
        
    def removeCostModifier(self, costMod):
        """ Remove the Cost Modifier from the Cost Calcualtor """
        if costMod in self.costModifiers:
            self.costModifiers.remove(costMod)