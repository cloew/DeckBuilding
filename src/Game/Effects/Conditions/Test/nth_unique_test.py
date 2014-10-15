import unittest

from Game.Effects.Conditions.nth_unique import NthUnique
from Game.Effects.Conditions.Filters.Criteria.fixed_criteria import FixedCriteria
from Game.Events.cards_event import CardsEvent
from Game.Sources.source_types import EVENT, PLAYED
from Test.builders import BuildPlayerContext, BuildCard

class evaluate(unittest.TestCase):
    """ Test cases of evaluate """
    
    def  setUp(self):
        """ Build the Context for the test """
        self.name = "Test Name"
        self.cardType = "A Type"
        self.event = CardsEvent([BuildCard(self.name, cardType=self.cardType)], None, BuildPlayerContext())
        
    def isNthUnique(self):
        """ Test that the condition is true when the card is the nth unique card played """
        n = 3
        playedSource = self.event.context.loadSource(PLAYED)
        [playedSource.add(BuildCard(self.name+str(i))) for i in range(n-1)]
        
        result = NthUnique(n, []).evaluate(self.event.context)
        self.assertTrue(result, "When the Event card matches the criteria and is the nth uniquely named card, the condition should be true")
        
    def isNotNthUnique(self):
        """ Test that the condition is false when the card is not the nth unique card played """
        n = 2
        playedSource = self.event.context.loadSource(PLAYED)
        [playedSource.add(BuildCard(self.name)) for i in range(n-1)]
        
        result = NthUnique(n, []).evaluate(self.event.context)
        self.assertFalse(result, "When the Event card matches the criteria and is not the nth uniquely named card, the condition should be false")
        
    def notMatchingCriteria(self):
        """ Test that the condition is false when the card is not the nth unique card played """
        n = 1
        type ="Equipment"
        result = NthUnique(n, [FixedCriteria("cardType", self.cardType + "Gibberish", "==")]).evaluate(self.event.context)
        self.assertFalse(result, "When the Event card does not match the criteria and is the nth uniquely named card, the condition should be false")

# Collect all test cases in this class
testcasesEvaluate = ["isNthUnique", "isNotNthUnique", "notMatchingCriteria"]
suiteEvaluate = unittest.TestSuite(map(evaluate, testcasesEvaluate))

##########################################################

# Collect all test cases in this file
suites = [suiteEvaluate]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)