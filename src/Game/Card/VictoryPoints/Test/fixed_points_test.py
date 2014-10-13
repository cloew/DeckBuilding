import unittest

from Game.Card.VictoryPoints.fixed_points import FixedPoints

class calculatePoints(unittest.TestCase):
    """ Test cases of calculatePoints """
    
    def  setUp(self):
        """ Build the Fixed Points Calculator for the test """
        self.points = 5
        self.pointsCalculator = FixedPoints(self.points)
        
    def basicPoints(self):
        """ Test that the basic points are returned """
        points = self.pointsCalculator.calculatePoints(None)
        self.assertEquals(points, self.points, "The Points should be the points of the Fixed Points Calculator")

# Collect all test cases in this class
testcasesCalculatePoints = ["basicPoints"]
suiteCalculatePoints = unittest.TestSuite(map(calculatePoints, testcasesCalculatePoints))

##########################################################

# Collect all test cases in this file
suites = [suiteCalculatePoints]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)