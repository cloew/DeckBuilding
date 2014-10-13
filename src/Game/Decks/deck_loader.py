from kao_deck.deck import Deck

class DeckLoader:
    """ Represents a standard method for loading a deck """
    
    def __init__(self, deckInitializer):
        """ Initialize the Deck Loader """
        self.deckInitializer = deckInitializer
        
    def loadDeck(self):
        """ Load the Deck """
        return Deck(deck_initializer=self.deckInitializer)