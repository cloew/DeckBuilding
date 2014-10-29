
class MultiSourceEvent:
    """ Represents an Event to wrap cards from multiple sources """
    
    def __init__(self, sources, context):
        """ Initialize the Cards Event with the cards and where they came from """
        self.sources = sources
        self.context = context.copy()
        self.context.event = self
        
    def remove(self, card):
        """ Remove the card from the deck """
        for source in self.sources:
            if card in source:
                source.remove(card)
                return
        
    def __getitem__(self, index):
        """ Return the item at the given index """
        return self.cards[index]
        
    def __len__(self):
        """ Return the length of the event """
        return len(self.cards)
        
    def __iter__(self):
        """ Return the iterator for the event when it is used as a source """
        return self.cards.__iter__()
        
    @property
    def cards(self):
        """ Return the cards from the event """
        return [card for source in self.sources for card in source]
        
    def cardsForPlayer(self, player):
        """ Return the cards in the source for the given player """
        sources = [source for source in self.sources if source.player is player]
        return [card for source in sources for card in source]