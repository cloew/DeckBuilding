import unittest

from Game.Card.VictoryPoints.per_result_points import PerResultPoints
from Test.dummy_filter import DummyFilter

class calculatePoints(unittest.TestCase):
    """ Test cases of calculatePoints """
    
    def  setUp(self):
        """ Build the Filter for the test """
        self.resultCount = 5
        self.filter = DummyFilter(self.resultCount)
        
    def perMatch(self):
        """ Test that the points matches the number of results from a filter """
        points = PerResultPoints(self.filter).calculatePoints(None)
        self.assertEquals(points, self.resultCount, "The Points should be the number of results from the filter")
        
    def pointsPerMatch(self):
        """ Test that the points matches the number of results from a filter """
        pointsPerMatch = 4
        points = PerResultPoints(self.filter, points=pointsPerMatch).calculatePoints(None)
        self.assertEquals(points, self.resultCount*pointsPerMatch, "The Points should be the number of results from the filter times the points per match provided")

# Collect all test cases in this class
testcasesCalculatePoints = ["perMatch", "pointsPerMatch"]
suiteCalculatePoints = unittest.TestSuite(map(calculatePoints, testcasesCalculatePoints))

##########################################################

# Collect all test cases in this file
suites = [suiteCalculatePoints]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)