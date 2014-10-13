from deck_loader import DeckLoader
from kao_deck.deck_with_discard_pile import DeckWithDiscardPile

class StartingDeckLoader(DeckLoader):
    """ Represents a standard method for loading a deck """
        
    def loadDeck(self):
        """ Load the Deck """
        return DeckWithDiscardPile(deck_initializer=self.deckInitializer, reshuffle=True)