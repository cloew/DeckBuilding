import unittest

from Game.Effects.Conditions.Filters.Operations.operations import inOperator as inOperatorMethod
from Game.Effects.Conditions.Filters.Operations.operations import compareEvenOrOdd as compareEvenOrOddMethod

class inOperator(unittest.TestCase):
    """ Test cases of inOperator """
    
    def  setUp(self):
        """ Build the value and container for the test """
        self.value = 1
        self.container = [1,2,3,4,5]
        
    def contains(self):
        """ Test that a value in the container returns true """
        isIn = inOperatorMethod(self.value, self.container)
        self.assertTrue(isIn, "If the value is in the container it should return true")
        
    def doesNotContain(self):
        """ Test that a value not in the container returns false """
        isIn = inOperatorMethod(self.value-1, self.container)
        self.assertFalse(isIn, "If the value is not in the container it should return false")

# Collect all test cases in this class
testcasesInOperator = ["contains", "doesNotContain"]
suiteInOperator = unittest.TestSuite(map(inOperator, testcasesInOperator))

##########################################################

class compareEvenOrOdd(unittest.TestCase):
    """ Test cases of compareEvenOrOdd """
        
    def valueIsEven(self):
        """ Test that the method returns true when the value is even """
        isEven = compareEvenOrOddMethod(0, "EVEN")
        self.assertTrue(isEven, "If the value and the expected value are even it should return true")
        
    def valueIsNotEven(self):
        """ Test that the method returns true when the value is even """
        isEven = compareEvenOrOddMethod(1, "EVEN")
        self.assertFalse(isEven, "If the value is not even and the expected value is it should return false")
        
    def valueIsOdd(self):
        """ Test that the method returns true when the value is odd """
        isOdd = compareEvenOrOddMethod(1, "ODD")
        self.assertTrue(isOdd, "If the value and the expected value are odd it should return true")
        
    def valueIsNotOdd(self):
        """ Test that the method returns true when the value is odd """
        isOdd = compareEvenOrOddMethod(0, "ODD")
        self.assertFalse(isOdd, "If the value is not odd and the expected value is it should return false")

# Collect all test cases in this class
testcasesCompareEvenOrOdd = ["valueIsEven", "valueIsNotEven", "valueIsOdd", "valueIsNotOdd"]
suiteCompareEvenOrOdd = unittest.TestSuite(map(compareEvenOrOdd, testcasesCompareEvenOrOdd))

##########################################################

# Collect all test cases in this file
suites = [suiteInOperator,
          suiteCompareEvenOrOdd]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)