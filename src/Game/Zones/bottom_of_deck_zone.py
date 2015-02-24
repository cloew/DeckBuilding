from zone import Zone

class BottomOfDeckZone(Zone):
    """ Represents the bottom of a Deck that can be used as a Zone """
    
    def __init__(self, deck, player, zoneType=None):
        """ Initialize the Deck Zone """
        self.deck = deck
        Zone.__init__(self, deck, player, zoneType=zoneType)
        
    def add(self, card):
        """ Add the given card to the zone """
        self.deck.putOnBottom(card)
        
    def __repr__(self):
        return '<Bottom of Deck:[' + ", ".join([str(item) for item in self.deck]) + ']>'