from zone import Zone

class ListZone(Zone):
    """ Represents a List that can be used as a Zone """
    
    def __init__(self, cards, zoneType=None):
        """ Initialize the Deck Zone """
        self.cards = cards
        Zone.__init__(self, cards, zoneType=zoneType)
        
    def add(self, card):
        """ Add the given card to the zone """
        self.cards.append(card)