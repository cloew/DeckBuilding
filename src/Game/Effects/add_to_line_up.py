
class AddToLineUp:
    """ Represents an effect to Add a Card to the Line Up """
    
    def __init__(self, count=None):
        """ Initialize the Effect with the number of cards to draw """
        if count is None:
            count = 1
        self.count = count
        
    def perform(self, args):
        """ Perform the Game Effect """
        args.game.lineUp.refillCards(self.count)