import unittest

from Game.Effects.Conditions.matching import Matching
from Game.Effects.Conditions.Filters.Criteria.fixed_criteria import FixedCriteria
from Game.Events.cards_event import CardsEvent
from Game.Sources.source_types import EVENT
from Test.builders import BuildPlayerContext, BuildCard

class evaluate(unittest.TestCase):
    """ Test cases of evaluate """
        
    def matching(self):
        """ Test that the condition is true, if there are enough matching cards """
        event = CardsEvent([1], None, BuildPlayerContext())
        result = Matching(EVENT).evaluate(event.context)
        self.assertTrue(result, "The Condition should be true, if there are enough matching cards")
        
    def notEnoughMatches(self):
        """ Test that the condition is false, if there are not enough matching cards """
        cards = [1,2,3]
        event = CardsEvent(cards, None, BuildPlayerContext())
        result = Matching(EVENT, number=len(cards)+1).evaluate(event.context)
        self.assertFalse(result, "The Condition should be false, if there are not enough matching cards")
        
    def criteriaUsed(self):
        """ Test that the condition is false, if the criteria limits the matches below the required number """
        name = "Test Name"
        cards = [BuildCard(name=name) for i in range(10)]
        event = CardsEvent(cards, None, BuildPlayerContext())
        result = Matching(EVENT, criteria=FixedCriteria("name", name, "!=")).evaluate(event.context)
        self.assertFalse(result, "The Condition should be false, if the criteria limits the matching cards")

# Collect all test cases in this class
testcasesEvaluate = ["matching", "notEnoughMatches", "criteriaUsed"]
suiteEvaluate = unittest.TestSuite(map(evaluate, testcasesEvaluate))

##########################################################

# Collect all test cases in this file
suites = [suiteEvaluate]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)