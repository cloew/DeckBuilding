
class BuyCard:
    """ Represents a command to buy a card """
    
    def __init__(self, card, owner, source):
        """ Initialize the Buy Card Command """
        self.card = card
        self.owner = owner
        self.source = source
        
    def perform(self):
        """ Perform the command """
        self.owner.spendPower(self.card.calculateCost())
        self.source.remove(self.card)
        self.owner.gainCard(self.card)