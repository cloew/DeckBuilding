from deck_source import DeckSource

class DeckWithDiscardPileSource(DeckSource):
    """ Represents a Deck with a discard pile that can be used as a Source """
    
    def availableLength(self):
        """ Return the number of available cards """
        return self.deck.availableLength()