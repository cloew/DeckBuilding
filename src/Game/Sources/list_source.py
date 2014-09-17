from source import Source

class ListSource(Source):
    """ Represents a List that can be used as a Source """
    
    def __init__(self, cards):
        """ Initialize the Deck Source """
        self.cards = cards
        Source.__init__(self, cards)
        
    def add(self, card):
        """ Add the given card to the source """
        self.cards.append(card)