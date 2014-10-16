import unittest

from Game.Effects.Activatables.activatable import Activatable
from Test.always_false_condition import AlwaysFalseCondition
from Test.always_true_condition import AlwaysTrueCondition
from Test.builders import BuildGame, BuildPlayerContext
from Test.coroutine_helper import RunCoroutine
from Test.dummy_effect import DummyEffect

class canActivate(unittest.TestCase):
    """ Test cases of canActivate """
    
    def setUp(self):
        """ Build the game for the test """
        self.game = BuildGame()
        self.effects = []
        
    def noCondition(self):
        """ Test that the Activatable can be activated when it has no condition """
        result = Activatable(self.effects).canActivate(self.game)
        self.assertTrue(result, "The Activatable should be activatable")
        
    def conditionFailed(self):
        """ Test that the Activatable cannot be activated when the condition fails """
        result = Activatable(self.effects, condition=AlwaysFalseCondition()).canActivate(self.game)
        self.assertFalse(result, "The Activatable should not be activatable")
        
    def conditionPassed(self):
        """ Test that the Activatable can be activated when the condition passes """
        result = Activatable(self.effects, condition=AlwaysTrueCondition()).canActivate(self.game)
        self.assertTrue(result, "The Activatable should be activatable")

# Collect all test cases in this class
testcasesCanActivate = ["noCondition", "conditionFailed", "conditionPassed"]
suiteCanActivate = unittest.TestSuite(map(canActivate, testcasesCanActivate))

##########################################################

class activate(unittest.TestCase):
    """ Test cases of activate """
    
    def setUp(self):
        """ Build the Game, Context, and Effects for the test """
        self.game = BuildGame()
        self.context = BuildPlayerContext()
        self.effects = [DummyEffect() for i in range(10)]
        
        self.calledUnregisterActivatable = False
        self.context.owner.unregisterActivatable = self.unregisterActivatable
        
    def effectsPerformed(self):
        """ Test that the effects are performed """
        activatable = Activatable(self.effects)
        RunCoroutine(activatable.activate(self.context))
        self.assertTrue(all([effect.performed for effect in self.effects]), "All the effects should have been performed")
        self.assertFalse(self.calledUnregisterActivatable, "The Activatable should not have been unregistered")
        
    def effectsPerformed_SingleUse(self):
        """ Test that the effects are performed """
        activatable = Activatable(self.effects, singleUse=True)
        RunCoroutine(activatable.activate(self.context))
        self.assertTrue(all([effect.performed for effect in self.effects]), "All the effects should have been performed")
        self.assertTrue(self.calledUnregisterActivatable, "The Activatable should not have been registered")
        
    def unregisterActivatable(self, card):
        """ Unregister the Activatable """
        self.calledUnregisterActivatable = True

# Collect all test cases in this class
testcasesActivate = ["effectsPerformed", "effectsPerformed_SingleUse"]
suiteActivate = unittest.TestSuite(map(activate, testcasesActivate))

##########################################################

# Collect all test cases in this file
suites = [suiteCanActivate,
          suiteActivate]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)