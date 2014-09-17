from source import Source

class DeckSource(Source):
    """ Represents a Deck that can be used as a Source """
    
    def __init__(self, deck):
        """ Initialize the Deck Source """
        self.deck = deck
        Source.__init__(self, deck)
        
    def add(self, card):
        """ Add the given card to the source """
        self.deck.add([card])