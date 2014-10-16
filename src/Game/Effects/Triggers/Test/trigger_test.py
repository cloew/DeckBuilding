import unittest

from Game.Effects.Triggers.trigger import Trigger
from Game.Events.game_events import CARD_PLAYED
from Game.Events.played_card_event import PlayedCardEvent

from Test.always_false_condition import AlwaysFalseCondition
from Test.always_true_condition import AlwaysTrueCondition
from Test.builders import BuildPlayerContext
from Test.coroutine_helper import RunCoroutine
from Test.dummy_effect import DummyEffect

class receive(unittest.TestCase):
    """ Test cases of receive """
    
    def setUp(self):
        """ Build the Event for the test """
        self.event = PlayedCardEvent(None, BuildPlayerContext())
        self.effect = DummyEffect()
        self.calledUnregisterTrigger = False
        self.event.context.owner.unregisterTrigger = self.unregisterTrigger
        
    def firedMultiUse(self):
        """ Test that the trigger was fired """
        trigger = Trigger(CARD_PLAYED, self.effect)
        RunCoroutine(trigger.receive(self.event))
        
        self.assertTrue(self.effect.performed, "The Trigger Effect should have been performed")
        self.assertFalse(self.calledUnregisterTrigger, "The Trigger should not have been unregistered")
        
    def firedSingleUse(self):
        """ Test that the trigger was fired and unregistered """
        trigger = Trigger(CARD_PLAYED, self.effect, singleUse=True)
        RunCoroutine(trigger.receive(self.event))
        
        self.assertTrue(self.effect.performed, "The Trigger Effect should have been performed")
        self.assertTrue(self.calledUnregisterTrigger, "The Trigger should have been unregistered")
        
    def conditionFailed(self):
        """ Test that the trigger is not fired when the condition fails """
        trigger = Trigger(CARD_PLAYED, self.effect, condition=AlwaysFalseCondition())
        RunCoroutine(trigger.receive(self.event))
        
        self.assertFalse(self.effect.performed, "The Trigger Effect should not have been performed")
        self.assertFalse(self.calledUnregisterTrigger, "The Trigger should not have been unregistered")
        
    def conditionPassed(self):
        """ Test that the trigger is fired when the condition passes """
        trigger = Trigger(CARD_PLAYED, self.effect, condition=AlwaysTrueCondition())
        RunCoroutine(trigger.receive(self.event))
        
        self.assertTrue(self.effect.performed, "The Trigger Effect should have been performed")
        self.assertFalse(self.calledUnregisterTrigger, "The Trigger should not have been unregistered")
        
    def unregisterTrigger(self, trigger):
        """ Unregister the Trigger """
        self.calledUnregisterTrigger = True

# Collect all test cases in this class
testcasesReceive = ["firedMultiUse", "firedSingleUse", "conditionFailed", "conditionPassed"]
suiteReceive = unittest.TestSuite(map(receive, testcasesReceive))

##########################################################

# Collect all test cases in this file
suites = [suiteReceive]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)