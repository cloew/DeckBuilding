from shuffling_deck_loader import ShufflingDeckLoader

class FixedTopCardDeckLoader(ShufflingDeckLoader):
    """ Represents a method for loading a deck and shuffling it """
    
    def __init__(self, deckInitializer, topCard):
        """ Initialize the Deck Loader """
        ShufflingDeckLoader.__init__(self, deckInitializer)
        self.topCard = topCard
        
    def loadDeck(self):
        """ Load the Deck """
        deck = ShufflingDeckLoader.loadDeck(self)
        deck.add([self.topCard])
        return deck