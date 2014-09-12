
class ListSource:
    """ Represents a List that can be used as a Source """
    
    def __init__(self, cards):
        """ Initialize the Deck Source """
        self.cards = cards
        
    def add(self, card):
        """ Add the given card to the source """
        self.cards.append(card)
        
    def remove(self, card):
        """ Remove the card from the deck """
        self.cards.remove(card)
        
    def __getitem__(self, index):
        """ Return the item at the given index """
        return self.cards[index]
        
    def __iter__(self):
        """ Return the Cards Iterator """
        return self.cards.__iter__()
        
    def __len__(self):
        """ Return the Length of the Cards """
        return len(self.cards)