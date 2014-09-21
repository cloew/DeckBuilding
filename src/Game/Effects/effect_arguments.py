
class EffectArguments:
    """ Wrapper for the arguments to an effect """
    
    def __init__(self, game, parent, event=None, player=None):
        """ Initialize the Arguments """
        self.parent = parent
        self.game = game
        self.event = event
        
        if player is None:
            player = self.owner.player
        self.player = player
        
    @property
    def foes(self):
        """ Return the foes of the current player """
        return [player for player in self.game.players if player is not self.player]
        
    @property
    def owner(self):
        """ Return the owner aka the current turn """
        return self.game.currentTurn