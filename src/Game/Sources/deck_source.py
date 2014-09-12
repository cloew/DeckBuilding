
class DeckSource:
    """ Represents a Deck that can be used as a Source """
    
    def __init__(self, deck):
        """ Initialize the Deck Source """
        self.deck = deck
        
    def add(self, card):
        """ Add the given card to the source """
        self.deck.add([card])
        
    def remove(self, card):
        """ Remove the card from the deck """
        self.deck.remove(card)
        
    def __getitem__(self, index):
        """ Return the item at the given index """
        return self.deck[index]
        
    def __iter__(self):
        """ Return the Deck Iterator """
        return self.deck.__iter__()