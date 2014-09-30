
class Defend:
    """ Represents a Command to defend """
    
    def __init__(self, card, owner):
        """ Initialize the Defend Command """
        self.card = card
        self.owner = owner
        
    def perform(self):
        """ Perform the command """
        self.owner.continueCommand(self.card)