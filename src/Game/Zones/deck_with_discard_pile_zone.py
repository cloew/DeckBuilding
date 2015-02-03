from deck_zone import DeckZone

class DeckWithDiscardPileZone(DeckZone):
    """ Represents a Deck with a discard pile that can be used as a Zone """
    
    def availableLength(self):
        """ Return the number of available cards """
        return self.deck.availableLength()