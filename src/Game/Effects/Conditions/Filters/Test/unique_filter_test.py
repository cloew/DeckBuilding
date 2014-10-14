import unittest

from Game.Effects.Conditions.Filters.unique_filter import UniqueFilter
from Game.Events.cards_event import CardsEvent
from Game.Sources.source_types import EVENT
from Test.builders import BuildCard, BuildPlayerContext

class evaluate(unittest.TestCase):
    """ Test cases of evaluate """
    
    def  setUp(self):
        """ Build the Filter for the test """
        self.cardName = "Blah Blah"
        self.cards = [BuildCard(name=self.cardName) for i in range(10)]
        cardsEvent = CardsEvent(self.cards, None, BuildPlayerContext())
        self.context = cardsEvent.context
        
    def uniqueValues(self):
        """ Test that only the unique values are returned """
        filter = UniqueFilter("name", EVENT)
        results = filter.evaluate(self.context)
        self.assertEquals(len(results), 1, "The results should be a single value")
        self.assertEquals(results[0].name, self.cardName, "The results should have the proper name")

# Collect all test cases in this class
testcasesFunctionToTest = ["uniqueValues"]
suiteFunctionToTest = unittest.TestSuite(map(evaluate, testcasesFunctionToTest))

##########################################################

# Collect all test cases in this file
suites = [suiteFunctionToTest]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)