import unittest

from Game.line_up import LineUp
from Game.Effects.Conditions.full_line_up import FullLineUp
from Test.builders import BuildPlayerContext

class evaluate(unittest.TestCase):
    """ Test cases of evaluate """
        
    def full(self):
        """ Test that the condition returns true when the line up is full """
        context = BuildPlayerContext()
        [context.game.lineUp.add(i) for i in range(LineUp.LINE_UP_SIZE)]
        result = FullLineUp().evaluate(context)
        self.assertTrue(result, "The Condition should be true when the line up has the proper number of elements")
        
    def overfilled(self):
        """ Test that the condition returns true when the line up is overfilled """
        context = BuildPlayerContext()
        [context.game.lineUp.add(i) for i in range(LineUp.LINE_UP_SIZE+1)]
        result = FullLineUp().evaluate(context)
        self.assertTrue(result, "The Condition should be true when the line up has at least the proper number of elements")
        
    def underfilled(self):
        """ Test that the condition returns false when the line up is underfilled """
        context = BuildPlayerContext()
        [context.game.lineUp.add(i) for i in range(LineUp.LINE_UP_SIZE-1)]
        result = FullLineUp().evaluate(context)
        self.assertFalse(result, "The Condition should be false when the line up has too few elements")

# Collect all test cases in this class
testcasesEvaluate = ["full", "overfilled", "underfilled"]
suiteEvaluate = unittest.TestSuite(map(evaluate, testcasesEvaluate))

##########################################################

# Collect all test cases in this file
suites = [suiteEvaluate]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)