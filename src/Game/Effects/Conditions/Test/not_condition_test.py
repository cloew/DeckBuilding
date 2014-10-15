import unittest

from Game.Effects.Conditions.not_condition import NotCondition
from Test.always_false_condition import AlwaysFalseCondition
from Test.always_true_condition import AlwaysTrueCondition

class evaluate(unittest.TestCase):
    """ Test cases of evaluate """
        
    def falseToTrue(self):
        """ Test that false results get flipped to true """
        result = NotCondition(AlwaysFalseCondition()).evaluate(None)
        self.assertTrue(result, "The False result should be flipped to true")
        
    def trueToFalse(self):
        """ Test that true results get flipped to false """
        result = NotCondition(AlwaysTrueCondition()).evaluate(None)
        self.assertFalse(result, "The True result should be flipped to false")

# Collect all test cases in this class
testcasesEvaluate = ["falseToTrue", "trueToFalse"]
suiteEvaluate = unittest.TestSuite(map(evaluate, testcasesEvaluate))

##########################################################

# Collect all test cases in this file
suites = [suiteEvaluate]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)