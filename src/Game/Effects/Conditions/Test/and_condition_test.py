import unittest

from Game.Effects.Conditions.and_condition import AndCondition
from Test.always_false_condition import AlwaysFalseCondition
from Test.always_true_condition import AlwaysTrueCondition

class evaluate(unittest.TestCase):
    """ Test cases of evaluate """
    
    def  setUp(self):
        """ Build the Conditions for the test """
        self.conditions = [AlwaysTrueCondition() for i in range(10)]
        
    def allTrue(self):
        """ Test that the And Condition returns true when all its conditions are true """
        result = AndCondition(self.conditions).evaluate(None)
        self.assertTrue(result, "The And Condition should evaluate to true when all its conditions are true")
        
    def oneFalse(self):
        """ Test that the And Condition returns false when at least one of its conditions are false """
        result = AndCondition(self.conditions + [AlwaysFalseCondition()]).evaluate(None)
        self.assertFalse(result, "The And Condition should evaluate to true when at least one of its conditions are false")

# Collect all test cases in this class
testcasesEvaluate = ["allTrue", "oneFalse"]
suiteEvaluate = unittest.TestSuite(map(evaluate, testcasesEvaluate))

##########################################################

# Collect all test cases in this file
suites = [suiteEvaluate]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)