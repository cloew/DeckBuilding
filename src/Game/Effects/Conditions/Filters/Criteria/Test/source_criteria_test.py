import unittest

from Game.Effects.game_contexts import PlayerContext
from Game.Effects.Conditions.Filters.Criteria.source_criteria import SourceCriteria
from Game.Events.cards_event import CardsEvent
from Game.Sources.source_types import EVENT
from Test.builders import BuildCard, BuildPlayerContext

class compare(unittest.TestCase):
    """ Test cases of compare """
    
    def  setUp(self):
        """ Build the Source and Criteria for the test """
        self.cardName = "Blah Blah"
        cardsEvent = CardsEvent([BuildCard(name=self.cardName)], None, BuildPlayerContext())
        self.context = cardsEvent.context
        self.criteria = SourceCriteria("name", EVENT)
        
    def valid(self):
        """ Test that the comparison can return valid if the cards in the source are properly set """
        cardToCompareAgainst = BuildCard(name=self.cardName)
        isValid = self.criteria.compare(cardToCompareAgainst, self.context)
        self.assertTrue(isValid, "The Comparison should be valid when the field value is set properly")
        
    def invalid(self):
        """ Test that the comparison returns invalid """
        cardToCompareAgainst = BuildCard(name=self.cardName+"Gibberish")
        isValid = self.criteria.compare(cardToCompareAgainst, self.context)
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