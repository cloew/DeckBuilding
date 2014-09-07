
class Draw:
    """ Represents an effect to Draw Cards """
    
    def __init__(self, count=1):
        """ Initialize the Effect with the number of cards to draw """
        self.count = count
        
    def perform(self, owner, card):
        """ Perform the Game Effect """
        owner.draw(count=self.count)