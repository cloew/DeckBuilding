
class PickCard:
    """ Represents a Command to pick a card """
    
    def __init__(self, card, owner):
        """ Initialize the Pick Card Command """
        self.card = card
        self.owner = owner
        
    def perform(self):
        """ Perform the command """
        self.owner.continueCommand(self.card)