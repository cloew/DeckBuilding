import unittest

from Game.Effects.Conditions.Filters.intersection_filter import IntersectionFilter
from Test.dummy_filter import DummyFilter

class evaluate(unittest.TestCase):
    """ Test cases of evaluate """
    
    def  setUp(self):
        """ Build the Filters for the test """
        self.intersectionValues = [3, 4]
        self.filters = [DummyFilter(results=[1,2]+self.intersectionValues), DummyFilter(results=[5,6]+self.intersectionValues)]
        
    def intersectionReturned(self):
        """ Test that the intersection is returned """
        filter = IntersectionFilter(self.filters)
        results = filter.evaluate(None)
        self.assertEquals(results, self.intersectionValues, "The intersection values should be returned")

# Collect all test cases in this class
testcasesEvaluate = ["intersectionReturned"]
suiteEvaluate = unittest.TestSuite(map(evaluate, testcasesEvaluate))

##########################################################

# Collect all test cases in this file
suites = [suiteEvaluate]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)