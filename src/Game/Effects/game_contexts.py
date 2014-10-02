from Game.Sources.source_factory import SourceFactory

def GetPlayersStartingWith(player, players):
    """ Get the players in order starting with the given player """
    foes = [player]
    for i in range(len(players)-1):
        player = GetNextPlayer(player, players)
        foes.append(player)
    return foes

def GetNextPlayer(player, players):
    """ Get the player next to the given player """
    index = players.index(player)
    index = (index + 1) % len(players)
    return players[index]

class Context:
    """ Represents a Game Context """
    
    def loadSource(self, sourceType):
        """ Load the given source using this context """
        return SourceFactory.getSourceInContext(sourceType, self)
    
class PlayerContext(Context):
    """ Represents the game context for a particular player """
    
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
        foes = GetPlayersStartingWith(self.player, self.potentialPlayers)
        foes.remove(self.player)
        return foes
        
    @property
    def nextPlayer(self):
        """ Return the next player """
        return GetNextPlayer(self.player, self.potentialPlayers)
        
    @property
    def owner(self):
        """ Return the owner aka the current turn """
        return self.game.currentTurn
        
    def copy(self):
        """ Copy the Context """
        return PlayerContext(self.game, self.parent, event=self.event, player=self.player)
        
    def getPlayerContext(self, player):
        """ Get the Context for the given player """
        return PlayerContext(self.game, self.parent, event=self.event, player=player)

class SystemContext(Context):
    """ Represents the game context for the System to use """
    
    def __init__(self, game, parent, event=None):
        """ Initialize the Arguments """
        self.parent = parent
        self.game = game
        self.event = event
        self.player = None
        
    @property
    def foes(self):
        """ Return the foes of the current player """
        return GetPlayersStartingWith(self.owner.player, self.game.players)
        
    @property
    def owner(self):
        """ Return the owner aka the current turn """
        return self.game.currentTurn
        
    def copy(self):
        """ Copy the Conotext """
        return SystemContext(self.game, self.parent, event=self.event)
        
    def getPlayerContext(self, player):
        """ Get the Context for the given player """
        return PlayerContext(self.game, self.parent, event=self.event, player=player)