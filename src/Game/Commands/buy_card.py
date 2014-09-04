
class BuyCard:
    """ Represents a command to buy a card """
    
    def __init__(self, card, owner, lineUp):
        """ Initialize the Buy Card Command """
        self.card = card
        self.owner = owner
        self.lineUp = lineUp
        
    def perform(self):
        """ Perform the command """
        self.lineUp.remove(self.card)
        self.owner.gainCard(self.card)