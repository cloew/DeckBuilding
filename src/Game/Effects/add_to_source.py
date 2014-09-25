
class AddToSource:
    """ Represents an effect to Add a card to the source """
    
    def __init__(self, card, source):
        """ Initialize the Effect with the card and the source to add it to """
        self.card = card
        self.source = source
        
    def perform(self, args):
        """ Perform the Game Effect """
        self.source.add(self.card)