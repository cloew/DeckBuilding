import copy

class EffectArguments:
    """ Wrapper for the arguments to an effect """
    
    def __init__(self, game, parent, event=None, player=None, potentialPlayers=None):
        """ Initialize the Arguments """
        self.parent = parent
        self.game = game
        self.event = event
        
        if player is None:
            player = self.owner.player
        self.player = player
        
        if potentialPlayers is None:
            potentialPlayers = self.game.players
        self.potentialPlayers = potentialPlayers
        
    @property
    def foes(self):
        """ Return the foes of the current player """
        return [player for player in self.game.players if player is not self.player]
        
    @property
    def nextPlayer(self):
        """ Return the next player """
        return self.getNextPlayer(self.player)
            
    def getNextPlayer(self, player):
        """ Get the player next to the given player """
        index = self.potentialPlayers.index(player)
        index = (index + 1) % len(self.potentialPlayers)
        return self.potentialPlayers[index]
        
    @property
    def owner(self):
        """ Return the owner aka the current turn """
        return self.game.currentTurn
        
    def copy(self):
        """ Copy the Arguments """
        return EffectArguments(self.game, self.parent, event=self.event, player=self.player)

class SystemEffectArguments:
    """ Wrapper for the arguments to an effect for the System to use """
    
    def __init__(self, game, parent, event=None):
        """ Initialize the Arguments """
        self.parent = parent
        self.game = game
        self.event = event
        self.player = None
        
    @property
    def foes(self):
        """ Return the foes of the current player """
        return self.game.players
        
    @property
    def owner(self):
        """ Return the owner aka the current turn """
        return self.game.currentTurn
        
    def copy(self):
        """ Copy the Arguments """
        return EffectArguments(self.game, self.parent, event=self.event, player=self.player)