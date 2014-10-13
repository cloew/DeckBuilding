import unittest

from Test.builders import BuildCharacter, BuildTurn, BuildPlayer

class addOngoingEffects(unittest.TestCase):
    """ Test cases of addOngoingEffects """
    
    def  setUp(self):
        """ Build the Character for the test """
        self.character = BuildCharacter()
        self.calledOngoingEffects = False
        
    def active(self):
        """ Test that the ongoing effects callback is used when the character is active """
        self.character.addOngoingEffects(self.addOngoingEffects)
        self.assertTrue(self.calledOngoingEffects, "The Add Ongoing Effects callback should have been called")
        
    def inactive(self):
        """ Test that the ongoing effects callback is not used when the character is inactive """
        self.character.deactivate()
        self.character.addOngoingEffects(self.addOngoingEffects)
        self.assertFalse(self.calledOngoingEffects, "The Add Ongoing Effects callback should not have been called")
        
    def addOngoingEffects(self, character):
        """ Callback to add Ongoing Effects """
        self.calledOngoingEffects = True

# Collect all test cases in this class
testcasesAddOngoingEffects = ["active", "inactive"]
suiteAddOngoingEffects = unittest.TestSuite(map(addOngoingEffects, testcasesAddOngoingEffects))

##########################################################

class activate(unittest.TestCase):
    """ Test cases of activate """
    
    def  setUp(self):
        """ Build the Character for the test """
        self.character = BuildCharacter()
        self.calledOngoingEffects = False
        
    def activated(self):
        """ Test that the character does not call addOngoingEffects when its re-activated on a different turn """
        turn = BuildTurn()
        turn.addOngoingEffects = self.addOngoingEffects
        
        self.character.deactivate()
        self.character.activate(turn)
        
        self.assertFalse(self.calledOngoingEffects, "The Add Ongoing Effects callback should not have been called")
        
    def reactivatedOnPlyersTurn(self):
        """ Test that the character calls addOngoingEffects when its re-activated on their turn """
        turn = BuildTurn(player=BuildPlayer(character=self.character))
        turn.addOngoingEffects = self.addOngoingEffects
        
        self.character.deactivate()
        self.character.activate(turn)
        
        self.assertTrue(self.calledOngoingEffects, "The Add Ongoing Effects callback should have been called")
        
    def addOngoingEffects(self, character):
        """ Callback to add Ongoing Effects """
        self.calledOngoingEffects = True

# Collect all test cases in this class
testcasesActivate = ["activated", "reactivatedOnPlyersTurn"]
suiteActivate = unittest.TestSuite(map(activate, testcasesActivate))

##########################################################

class deactivate(unittest.TestCase):
    """ Test cases of deactivate """
    
    def  setUp(self):
        """ Build the Character for the test """
        self.character = BuildCharacter()
        
    def deactivated(self):
        """ Test that the character was deactivated """
        self.character.deactivate()
        self.assertFalse(self.character.active, "The Character should not be active after deactivating")

# Collect all test cases in this class
testcasesDeactivate = ["deactivated"]
suiteDeactivate = unittest.TestSuite(map(deactivate, testcasesDeactivate))

##########################################################

# Collect all test cases in this file
suites = [suiteAddOngoingEffects,
          suiteActivate,
          suiteDeactivate]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)