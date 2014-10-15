import unittest

from Game.Effects.Conditions.enough_power import EnoughPower
from Test.builders import BuildPlayerContext

class evaluate(unittest.TestCase):
    """ Test cases of evaluate """
    
    def  setUp(self):
        """ Build the Condition and Context for the test """
        self.neededPower = 4
        self.condition = EnoughPower(self.neededPower)
        self.context = BuildPlayerContext()
        
    def enoughPower(self):
        """ Test that if the current player has enough power, the condition returns true """
        self.context.owner.gainPower(None, self.neededPower)
        result = self.condition.evaluate(self.context)
        self.assertTrue(result, "The Condition should evaluate to true when the turn has enough power")
        
    def notEnoughPower(self):
        """ Test that if the current player does not have enough power, the condition returns false """
        self.context.owner.gainPower(None, self.neededPower-1)
        result = self.condition.evaluate(self.context)
        self.assertFalse(result, "The Condition should evaluate to false when the turn does not have enough power")

# Collect all test cases in this class
testcasesFunctionToTest = ["enoughPower", "notEnoughPower"]
suiteFunctionToTest = unittest.TestSuite(map(evaluate, testcasesFunctionToTest))

##########################################################

# Collect all test cases in this file
suites = [suiteFunctionToTest]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)