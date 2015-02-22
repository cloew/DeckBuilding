from Game.Zones.zone_types import EVENT

class CardsEvent:
    """ Represents an Event to wrap an arbitrary number of cards """
    
    def __init__(self, cards, fromZone, context):
        """ Initialize the Cards Event with the cards and where they came from """
        self.cards = list(cards)
        self.fromZone = fromZone
        
        self.context = context.copy()
        self.context.event = self
    
    def add(self, card):
        """ Add the card from the deck """
        self.fromZone.add(card)    
        
    def remove(self, card):
        """ Remove the card from the deck """
        self.fromZone.remove(card)
        
    def __getitem__(self, index):
        """ Return the item at the given index """
        return self.cards[index]
        
    def __len__(self):
        """ Return the length of the event """
        return len(self.cards)
        
    def __iter__(self):
        """ Return the iterator for the event when it is used as a source """
        return self.cards.__iter__()
        
    def loadZone(self):
        """ Load the Event Zone """
        return self.context.loadZone(EVENT)
        
    @property
    def player(self):
        """ Return the current player """
        return self.context.player