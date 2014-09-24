
class PickCard:
    """ Represents a Command to pick a card """
    
    def __init__(self, cards, owner):
        """ Initialize the Pick Card Command """
        self.cards = cards
        self.owner = owner
        
    def perform(self):
        """ Perform the command """
        self.owner.continueCommand(self.cards)