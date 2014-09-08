
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
            
    def remove(self, card):
        """ Remove a card from the line-up """
        self.cards.remove(card)
        
    def __iter__(self):
        """ Return the Line-up Iterator """
        return self.cards.__iter__()