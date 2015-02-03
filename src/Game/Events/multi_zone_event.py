
class MultiZoneEvent:
    """ Represents an Event to wrap cards from multiple zones """
    
    def __init__(self, zones, context):
        """ Initialize the Cards Event with the cards and where they came from """
        self.zones = zones
        self.context = context.copy()
        self.context.event = self
        
    def remove(self, card):
        """ Remove the card from the deck """
        for zone in self.zones:
            if card in zone:
                zone.remove(card)
                return
        
    def __getitem__(self, index):
        """ Return the item at the given index """
        return self.cards[index]
        
    def __len__(self):
        """ Return the length of the event """
        return len(self.cards)
        
    def __iter__(self):
        """ Return the iterator for the event when it is used as a zone """
        return self.cards.__iter__()
        
    @property
    def cards(self):
        """ Return the cards from the event """
        return [card for zone in self.zones for card in zone]
        
    def cardsForPlayer(self, player):
        """ Return the cards in the zone for the given player """
        zones = [zone for zone in self.zones if zone.player is player]
        return [card for zone in zones for card in zone]