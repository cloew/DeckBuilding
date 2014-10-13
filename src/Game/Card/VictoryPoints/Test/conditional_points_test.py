import unittest

from Game.Card.VictoryPoints.conditional_points import ConditionalPoints
from Game.Card.VictoryPoints.fixed_points import FixedPoints
from Test.always_false_condition import AlwaysFalseCondition
from Test.always_true_condition import AlwaysTrueCondition

class calculatePoints(unittest.TestCase):
    """ Test cases of calculatePoints """
    
    def  setUp(self):
        """ Build the VP Calculator for the test """
        self.truePoints = 5
        self.truePointsCalculator = FixedPoints(self.truePoints)
        
        self.falsePoints = self.truePoints + 1
        self.falsePointsCalculator = FixedPoints(self.falsePoints)
        
    def trueConditionPoints(self):
        """ Test that when the condition is true the points are returned properly """
        pointsCalculator = ConditionalPoints(AlwaysTrueCondition(), self.truePointsCalculator, self.falsePointsCalculator)
        points = pointsCalculator.calculatePoints(None)
        self.assertEquals(points, self.truePoints, "The Points should be the points for when the Conditional Points Calculator Condition is true")
        
    def falseConditionPoints(self):
        """ Test that when the condition is true the points are returned properly """
        pointsCalculator = ConditionalPoints(AlwaysFalseCondition(), self.truePointsCalculator, self.falsePointsCalculator)
        points = pointsCalculator.calculatePoints(None)
        self.assertEquals(points, self.falsePoints, "The Points should be the points for when the Conditional Points Calculator Condition is false")

# Collect all test cases in this class
testcasesCalculatePoints = ["trueConditionPoints", "falseConditionPoints"]
suiteCalculatePoints = unittest.TestSuite(map(calculatePoints, testcasesCalculatePoints))

##########################################################

# Collect all test cases in this file
suites = [suiteCalculatePoints]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)