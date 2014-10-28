from deck_loader import DeckLoader

class ShufflingDeckLoader(DeckLoader):
    """ Represents a method for loading a deck and shuffling it """
        
    def loadDeck(self, **kwargs):
        """ Load the Deck """
        deck = DeckLoader.loadDeck(self, **kwargs)
        deck.shuffle()
        return deck