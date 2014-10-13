import unittest

from Game.Decks.fixed_top_card_deck_loader import FixedTopCardDeckLoader
from kao_deck.deck_initializer import DeckInitializer

class loadDeck(unittest.TestCase):
    """ Test cases of loadDeck """
    
    def  setUp(self):
        """ Build the Deck Loader for the test """
        self.topItem = 1
        self.items = [2,3,4,5]
        deckInitializer = DeckInitializer()
        [deckInitializer.addItem(item, 1) for item in self.items]
        
        self.deckLoader = FixedTopCardDeckLoader(deckInitializer, self.topItem)
        
    def deckCreated(self):
        """ Test that the deck was created properly """
        deck = self.deckLoader.loadDeck()
        self.assertTrue(all([item in deck for item in self.items]), "Each item in the deck initializer should be in the deck")
        self.assertEquals(self.topItem, deck[0], "The Top Item should be the top item provided to the deck loader")

# Collect all test cases in this class
testcasesLoadDeck = ["deckCreated"]
suiteLoadDeck = unittest.TestSuite(map(loadDeck, testcasesLoadDeck))

##########################################################

# Collect all test cases in this file
suites = [suiteLoadDeck]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)