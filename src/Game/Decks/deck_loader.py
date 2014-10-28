from kao_deck.deck import Deck

class DeckLoader:
    """ Represents a standard method for loading a deck """
    
    def __init__(self, deckInitializer):
        """ Initialize the Deck Loader """
        self.deckInitializer = deckInitializer
        
    def loadDeck(self, number=None):
        """ Load the Deck """
        deck = self.buildDeck()
        if number is not None:
            items = deck.draw(count=number)
            deck = Deck(items=items)
        return deck
        
    def buildDeck(self):
        """ Build the Deck """
        return Deck(deck_initializer=self.deckInitializer)