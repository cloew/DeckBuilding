import unittest

from Game.Effects.Conditions.Filters.Criteria.fixed_criteria import FixedCriteria
from Test.builders import BuildCard

class compare(unittest.TestCase):
    """ Test cases of compare """
    
    def  setUp(self):
        """ Build the Card and Criteria for the test """
        self.cardName = "Blah Blah"
        self.card = BuildCard(name=self.cardName)
        
    def valid(self):
        """ Test that the comparison returns valid """
        criteria = FixedCriteria("name", self.cardName, "==")
        isValid = criteria.compare(self.card, None)
        self.assertTrue(isValid, "The Comparison should be valid when the field value is set properly")
        
    def invalid(self):
        """ Test that the comparison returns invalid """
        criteria = FixedCriteria("name", self.cardName + "Gibberish", "==")
        isValid = criteria.compare(self.card, None)
        self.assertFalse(isValid, "The Comparison should not be valid when the field value is set differently")

# Collect all test cases in this class
testcasesCompare = ["valid", "invalid"]
suiteCompare = unittest.TestSuite(map(compare, testcasesCompare))

##########################################################

# Collect all test cases in this file
suites = [suiteCompare]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)