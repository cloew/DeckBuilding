from Game.Sources.source_types import LINE_UP

class LineUp:
    """ Represents the Line Up of available cards in the game """
    LINE_UP_SIZE = 5
    
    def __init__(self, mainDeck):
        """ Initialize the Line Up with the main deck to pull from """
        self.mainDeck = mainDeck
        self.sourceType = LINE_UP
        self.cards = []
        self.refill()
        
    def refill(self):
        """ Refill the line-up """
        slotsToRefill = self.LINE_UP_SIZE - len(self.cards)
        if slotsToRefill > 0:
            self.refillCards(count=slotsToRefill)
            
    def refillCards(self, count):
        """ Refill the given number of cards """
        self.cards += self.mainDeck.draw(count=count)
            
    def add(self, card):
        """ Add a card to the line up """
        self.cards.append(card)
            
    def remove(self, card):
        """ Remove a card from the line-up """
        self.cards.remove(card)
        
    def isFull(self):
        """ Return if the Line Up is full """
        return len(self) == self.LINE_UP_SIZE
        
    def __getitem__(self, index):
        """ Return the item at the given index """
        return self.cards[index]
        
    def __len__(self):
        """ Return the length of the Line Up """
        return len(self.cards)
        
    def __iter__(self):
        """ Return the Line-up Iterator """
        return self.cards.__iter__()