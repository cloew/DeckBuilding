
class Defend:
    """ Represents a Command to defend """
    
    def __init__(self, card):
        """ Initialize the Defend Command """
        self.card = card
        
    def perform(self):
        """ Perform the command """
        self.owner.continueCommand(self.card)