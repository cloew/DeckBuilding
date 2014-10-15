import unittest

from Game.Effects.Conditions.unique import Unique
from Game.Effects.Conditions.Filters.Criteria.fixed_criteria import FixedCriteria
from Game.Events.cards_event import CardsEvent
from Game.Sources.source_types import EVENT, PLAYED
from Test.builders import BuildPlayerContext, BuildCard

class evaluate(unittest.TestCase):
    """ Test cases of evaluate """
    
    def  setUp(self):
        """ Build the Event for the test """
        self.field = "name"
        self.name = "Test Name"
        self.event = CardsEvent([BuildCard(self.name)], None, BuildPlayerContext())
        
    def isUnique(self):
        """ Test that a event with the specified unique field returns true """
        playedSource = self.event.context.loadSource(PLAYED)
        playedSource.add(BuildCard(self.name + "Gibberish"))
        
        result = Unique(self.field, PLAYED).evaluate(self.event.context)
        self.assertTrue(result, "When the Event card has the specified field as unique, the condition should be true")
        
    def isNotUnique(self):
        """ Test that a event without the specified unique field returns false """
        playedSource = self.event.context.loadSource(PLAYED)
        playedSource.add(BuildCard(self.name))
        
        result = Unique(self.field, PLAYED).evaluate(self.event.context)
        self.assertFalse(result, "When the Event card does have the specified field as unique, the condition should be false")

# Collect all test cases in this class
testcasesEvaluate = ["isUnique", "isNotUnique"]
suiteEvaluate = unittest.TestSuite(map(evaluate, testcasesEvaluate))

##########################################################

# Collect all test cases in this file
suites = [suiteEvaluate]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)