import unittest

from Game.Card.Cost.fixed_cost import FixedCost

class calculateCost(unittest.TestCase):
    """ Test cases of calculateCost """
    
    def  setUp(self):
        """ Build the Cost Calculator for the test """
        self.modifierCosts = [1, 2, 3, 4, 5]
        self.cost = 10
        self.costCalculator = FixedCost(self.cost)
        
        self.costCalculatorWithCostMods = FixedCost(self.cost)
        [self.costCalculatorWithCostMods.addCostModifier(FixedCost(cost)) for cost in self.modifierCosts]
        
        
    def basicCost(self):
        """ Test that the basic cost is returned proeprly """
        cost = self.costCalculator.calculateCost()
        self.assertEquals(cost, self.cost, "The Cost should be the cost of the Fixed Cost Calculator")
        
    def withCostMods(self):
        """ Test that the cost is returned proeprly with cost mods """
        cost = self.costCalculatorWithCostMods.calculateCost()
        self.assertEquals(cost, sum([self.cost] + self.modifierCosts), "The Cost should be the cost of the Fixed Cost Calculator and all of its Cost Mods")

# Collect all test cases in this class
testcasesCalculateCost = ["basicCost", "withCostMods"]
suiteCalculateCost = unittest.TestSuite(map(calculateCost, testcasesCalculateCost))

##########################################################

class addCostModifier(unittest.TestCase):
    """ Test cases of addCostModifier """
    
    def  setUp(self):
        """ Build the Cost Calculator and Modifier for the test """
        self.cost = 10
        self.costCalculator = FixedCost(self.cost)
        
    def added(self):
        """ Test that the Cost Modifier is added """
        costMod = FixedCost(1)
        self.costCalculator.addCostModifier(costMod)
        self.assertIn(costMod, self.costCalculator.costModifiers, "The Cost Mod should be added to the Cost Mods of the Fixed Cost Calculator")

# Collect all test cases in this class
testcasesAddCostModifier = ["added"]
suiteAddCostModifier = unittest.TestSuite(map(addCostModifier, testcasesAddCostModifier))

##########################################################

class removeCostModifier(unittest.TestCase):
    """ Test cases of removeCostModifier """
    
    def  setUp(self):
        """ Build the *** for the test """
        self.cost = 10
        self.costCalculator = FixedCost(self.cost)
        self.costMod = FixedCost(1)
        self.costCalculator.addCostModifier(self.costMod)
        
    def removed(self):
        """ Test that the Cost Mod is properly removed when it is added """
        self.costCalculator.removeCostModifier(self.costMod)
        self.assertNotIn(self.costMod, self.costCalculator.costModifiers, "The Cost Mod should be remvoed from the Cost Mods of the Fixed Cost Calculator")
        
    def notInCostMods(self):
        """ Test that no error is thrown when attempting to remove a Cost Mod that has not been added """
        costMod = FixedCost(1)
        self.costCalculator.removeCostModifier(costMod)

# Collect all test cases in this class
testcasesRemoveCostModifier = ["removed", "notInCostMods"]
suiteRemoveCostModifier = unittest.TestSuite(map(removeCostModifier, testcasesRemoveCostModifier))

##########################################################

# Collect all test cases in this file
suites = [suiteCalculateCost,
          suiteAddCostModifier,
          suiteRemoveCostModifier]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)