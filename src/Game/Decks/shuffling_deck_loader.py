from deck_loader import DeckLoader

class ShufflingDeckLoader(DeckLoader):
    """ Represents a method for loading a deck and shuffling it """
        
    def loadDeck(self):
        """ Load the Deck """
        deck = DeckLoader.loadDeck(self)
        deck.shuffle()
        return deck