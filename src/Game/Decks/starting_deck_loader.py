from shuffling_deck_loader import ShufflingDeckLoader
from kao_deck.deck_with_discard_pile import DeckWithDiscardPile

class StartingDeckLoader(ShufflingDeckLoader):
    """ Represents a standard method for loading a deck """
        
    def buildDeck(self):
        """ Load the Deck """
        return DeckWithDiscardPile(deck_initializer=self.deckInitializer, reshuffle=True)