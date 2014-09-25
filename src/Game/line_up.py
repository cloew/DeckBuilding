
class LineUp:
    """ Represents the Line Up of available cards in the game """
    LINE_UP_SIZE = 5
    
    def __init__(self, mainDeck):
        """ Initialize the Line Up with the main deck to pull from """
        self.mainDeck = mainDeck
        self.cards = []
        self.refill()
        
    def refill(self):
        """ Refill the line-up """
        slotsToRefill = self.LINE_UP_SIZE - len(self.cards)
        if slotsToRefill > 0:
            self.cards += self.mainDeck.draw(count=slotsToRefill)
            
    def add(self, card):
        """ Add a card to the line up """
        self.cards.append(card)
            
    def remove(self, card):
        """ Remove a card from the line-up """
        self.cards.remove(card)
        
    def __getitem__(self, index):
        """ Return the item at the given index """
        return self.cards[index]
        
    def __len__(self):
        """ Return the length of the Line Up """
        return len(self.cards)
        
    def __iter__(self):
        """ Return the Line-up Iterator """
        return self.cards.__iter__()