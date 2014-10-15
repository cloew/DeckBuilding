import unittest

from Game.Effects.Conditions.is_player_turn import IsPlayerTurn
from Test.builders import BuildPlayerContext, BuildPlayer

class evaluate(unittest.TestCase):
    """ Test cases of evaluate """
    
    def  setUp(self):
        """ Build the Condition for the test """
        self.condition = IsPlayerTurn()
        
    def isPlayerTurn(self):
        """ Test that the condition is true, if the player is the current player """
        context = BuildPlayerContext()
        context.player = context.owner.player
        result = self.condition.evaluate(context)
        self.assertTrue(result, "The condition should return true, if the player is the current turn's player")
        
    def isNotPlayerTurn(self):
        """ Test that the condition is false, if the player is not the current player """
        context = BuildPlayerContext()
        context.player = BuildPlayer()
        result = self.condition.evaluate(context)
        self.assertFalse(result, "The condition should return false, if the player is not the current turn's player")

# Collect all test cases in this class
testcasesEvaluate = ["isPlayerTurn", "isNotPlayerTurn"]
suiteEvaluate = unittest.TestSuite(map(evaluate, testcasesEvaluate))

##########################################################

# Collect all test cases in this file
suites = [suiteEvaluate]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)