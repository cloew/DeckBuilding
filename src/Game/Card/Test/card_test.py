import unittest

from Test.builders import BuildCard, BuildGame
from Test.dummy_effect import DummyEffect

class play(unittest.TestCase):
    """ Test cases of play """
    
    def  setUp(self):
        """ Build the Card for the test """
        self.card = BuildCard(playEffects=[DummyEffect() for i in range(10)])
        
    def playEffectsPerformed(self):
        """ Test that the card play effects were performed """
        coroutine = self.card.play(BuildGame())
        self.assertRaises(StopIteration, coroutine.next)
        self.assertTrue(all([effect.performed for effect in self.card.playEffects]), "All the effects should be performed")

# Collect all test cases in this class
testcasesPlay = ["playEffectsPerformed"]
suitePlay = unittest.TestSuite(map(play, testcasesPlay))

##########################################################

# Collect all test cases in this file
suites = [suitePlay]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)