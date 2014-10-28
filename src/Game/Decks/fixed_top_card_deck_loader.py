from shuffling_deck_loader import ShufflingDeckLoader

class FixedTopCardDeckLoader(ShufflingDeckLoader):
    """ Represents a method for loading a deck and shuffling it """
    
    def __init__(self, deckInitializer, topCard):
        """ Initialize the Deck Loader """
        ShufflingDeckLoader.__init__(self, deckInitializer)
        self.topCard = topCard
        
    def loadDeck(self, number=None):
        """ Load the Deck """
        if number is not None:
            number -= 1
        
        deck = ShufflingDeckLoader.loadDeck(self, number=number)
        deck.add([self.topCard])
        return deck