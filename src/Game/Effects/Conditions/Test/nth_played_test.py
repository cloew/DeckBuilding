import unittest

from Game.Effects.Conditions.nth_played import NthPlayed
from Game.Effects.Conditions.Filters.Criteria.fixed_criteria import FixedCriteria
from Game.Events.cards_event import CardsEvent
from Game.Sources.source_types import EVENT, PLAYED
from Test.builders import BuildPlayerContext, BuildCard
from Test.dummy_filter import DummyFilter

class evaluate(unittest.TestCase):
    """ Test cases of evaluate """
    
    def  setUp(self):
        """ Build the Context for the test """
        self.name = "Test Name"
        self.event = CardsEvent([BuildCard(self.name)], None, BuildPlayerContext())
        
    def isNthPlayed(self):
        """ Test that the condition is true when the card is the nth one played """
        n = 3
        playedSource = self.event.context.loadSource(PLAYED)
        [playedSource.add(BuildCard(self.name)) for i in range(n-1)]
        
        result = NthPlayed(n, FixedCriteria("name", self.name, "==")).evaluate(self.event.context)
        self.assertTrue(result, "When the Event card matches the criteria and is the nth card, the condition should be true")
        
    def notNthPlayed(self):
        """ Test that the condition is false when the card is not the nth one played """
        result = NthPlayed(2, FixedCriteria("name", self.name, "==")).evaluate(self.event.context)
        self.assertFalse(result, "When the Event card matches the criteria and is not the nth card, the condition should be false")
        
    def notMatchingCriteria(self):
        """ Test that the condition is false when the card does not match the criteria """
        result = NthPlayed(1, FixedCriteria("name", self.name, "!=")).evaluate(self.event.context)
        self.assertFalse(result, "When the Event card does not match the criteria and is the nth card, the condition should be false")

# Collect all test cases in this class
testcasesFunctionToTest = ["isNthPlayed", "notNthPlayed", "notMatchingCriteria"]
suiteFunctionToTest = unittest.TestSuite(map(evaluate, testcasesFunctionToTest))

##########################################################

# Collect all test cases in this file
suites = [suiteFunctionToTest]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)