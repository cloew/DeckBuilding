import unittest

from Game.Effects.Conditions.or_condition import OrCondition
from Test.always_false_condition import AlwaysFalseCondition
from Test.always_true_condition import AlwaysTrueCondition

class evaluate(unittest.TestCase):
    """ Test cases of evaluate """
    
    def  setUp(self):
        """ Build the Conditions for the test """
        self.conditions = [AlwaysFalseCondition() for i in range(10)]
        
    def oneTrue(self):
        """ Test that the Or Condition returns true when at least one of its conditions are true """
        result = OrCondition(self.conditions + [AlwaysTrueCondition()]).evaluate(None)
        self.assertTrue(result, "The And Condition should evaluate to true when at least one of its conditions are true")
        
    def allFalse(self):
        """ Test that the Or Condition returns false when aall of its conditions are false """
        result = OrCondition(self.conditions).evaluate(None)
        self.assertFalse(result, "The And Condition should evaluate to false when all of its conditions are false")

# Collect all test cases in this class
testcasesEvaluate = ["oneTrue", "allFalse"]
suiteEvaluate = unittest.TestSuite(map(evaluate, testcasesEvaluate))

##########################################################

# Collect all test cases in this file
suites = [suiteEvaluate]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)