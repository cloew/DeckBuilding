import unittest

from Game.Effects.Conditions.has_cards import HasCards
from Game.Events.cards_event import CardsEvent
from Game.Sources.source_types import EVENT
from Test.builders import BuildPlayerContext
from Test.dummy_filter import DummyFilter

class evaluate(unittest.TestCase):
    """ Test cases of evaluate """
        
    def hasCards(self):
        """ Test that if the source has cards, the condition returns true """
        event = CardsEvent([1,2,3], None, BuildPlayerContext())
        result = HasCards(EVENT).evaluate(event.context)
        self.assertTrue(result, "The Condition should be true, if the source has cards")
        
    def noCards(self):
        """ Test that if the source has no cards, the condition returns false """
        event = CardsEvent([], None, BuildPlayerContext())
        result = HasCards(EVENT).evaluate(event.context)
        self.assertFalse(result, "The Condition should be false, if the source has no cards")
        
    def filterHasCards(self):
        """ Test that if the filter returns cards, the condition returns true """
        event = CardsEvent([1,2,3], None, BuildPlayerContext())
        result = HasCards(EVENT, filter=DummyFilter(results=[1,2,3])).evaluate(event.context)
        self.assertTrue(result, "The Condition should be true, if the filter returns cards")
        
    def emptyFilter(self):
        """ Test that if the filter returns no cards, the condition returns false """
        event = CardsEvent([], None, BuildPlayerContext())
        result = HasCards(EVENT, filter=DummyFilter()).evaluate(event.context)
        self.assertFalse(result, "The Condition should be false, if the filter returns no cards")

# Collect all test cases in this class
testcasesEvaluate = ["hasCards", "noCards", "filterHasCards", "emptyFilter"]
suiteEvaluate = unittest.TestSuite(map(evaluate, testcasesEvaluate))

##########################################################

# Collect all test cases in this file
suites = [suiteEvaluate]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)