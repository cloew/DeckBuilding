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
        
    def putOnBottom(self, card):
        """ Add the given card to the bottom of the source """
        self.deck.putOnBottom(card)
        
    def __repr__(self):
        return '<Deck:[' + ", ".join([str(item) for item in self.deck]) + ']>'