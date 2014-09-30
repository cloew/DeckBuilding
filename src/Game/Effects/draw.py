
class Draw:
    """ Represents an effect to Draw Cards """
    
    def __init__(self, count=1):
        """ Initialize the Effect with the number of cards to draw """
        self.count = count
        
    def perform(self, args):
        """ Perform the Game Effect """
        args.player.draw(count=self.count)