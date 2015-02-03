from zone import Zone

class DeckZone(Zone):
    """ Represents a Deck that can be used as a Zone """
    
    def __init__(self, deck, zoneType=None):
        """ Initialize the Deck Zone """
        self.deck = deck
        Zone.__init__(self, deck, zoneType=zoneType)
        
    def add(self, card):
        """ Add the given card to the zone """
        self.deck.add([card])
        
    def putOnBottom(self, card):
        """ Add the given card to the bottom of the zone """
        self.deck.putOnBottom(card)
        
    def __repr__(self):
        return '<Deck:[' + ", ".join([str(item) for item in self.deck]) + ']>'