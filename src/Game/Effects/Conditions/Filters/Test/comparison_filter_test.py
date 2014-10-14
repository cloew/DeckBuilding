import unittest

from Game.Effects.game_contexts import PlayerContext
from Game.Effects.Conditions.Filters.Criteria.fixed_criteria import FixedCriteria
from Game.Effects.Conditions.Filters.comparison_filter import ComparisonFilter
from Game.Events.cards_event import CardsEvent
from Game.Sources.source_types import EVENT
from Test.builders import BuildCard, BuildPlayerContext
from Test.always_false_criteria import AlwaysFalseCriteria
from Test.always_true_criteria import AlwaysTrueCriteria

class evaluate(unittest.TestCase):
    """ Test cases of evaluate """
    
    def  setUp(self):
        """ Build the Filter for the test """
        self.cardName = "Blah Blah"
        self.cards = [BuildCard(name=self.cardName) for i in range(10)]
        cardsEvent = CardsEvent(self.cards, None, BuildPlayerContext())
        self.context = cardsEvent.context
        
    def matching(self):
        """ Test that all matching results are returned by the filter """
        filter = ComparisonFilter(EVENT, AlwaysTrueCriteria())
        results = filter.evaluate(self.context)
        self.assertEquals(results, self.cards, "All the cards should be returned")
        
    def notMatching(self):
        """ Test that all matching results are returned by the filter """
        filter = ComparisonFilter(EVENT, AlwaysFalseCriteria())
        results = filter.evaluate(self.context)
        self.assertEquals(results, [], "No cards should be returned")

# Collect all test cases in this class
testcasesEvaluate = ["matching", "notMatching"]
suiteEvaluate = unittest.TestSuite(map(evaluate, testcasesEvaluate))

##########################################################

# Collect all test cases in this file
suites = [suiteEvaluate]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)