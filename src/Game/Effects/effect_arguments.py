
class EffectArguments:
    """ Wrapper for the arguments to an effect """
    
    def __init__(self, game, parent, event=None):
        """ Initialize the Arguments """
        self.parent = parent
        self.game = game
        self.event = event
        
    @property
    def owner(self):
        """ Return the owner aka the current turn """
        return self.game.currentTurn