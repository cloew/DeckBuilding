from context import Context

from Game.player_order_helper import GetPlayersStartingWith, GetNextPlayer, GetPreviousPlayer

from kao_decorators import smart_defaults, Default

CopyContextDefaults = [Default('parent', field='parent'), Default('event', field='event'), Default('foes', field='foes')]

def GetPlayerFoes(currentPlayer, players):
    """ Return the foes for the given player """
    foes = GetPlayersStartingWith(currentPlayer, players)
    foes.remove(currentPlayer)
    return foes

class PlayerContext(Context):
    """ Represents the game context for a particular player """
    
    def __init__(self, game, parent, event=None, player=None, foes=None):
        """ Initialize the Arguments """
        Context.__init__(self, game, parent, event=event)
        
        if player is None:
            player = self.owner.player
        self.player = player
        
        if foes is None:
            foes = GetPlayerFoes(self.player, self.game.players)
        self.foes = foes
        
    @property
    def nextPlayer(self):
        """ Return the next player """
        return GetNextPlayer(self.player, self.potentialPlayers)
        
    @property
    def previousPlayer(self):
        """ Return the previous player """
        return GetPreviousPlayer(self.player, self.potentialPlayers)
        
    @property
    def potentialPlayers(self):
        """ Return the players available in the current context """
        return [self.player] + self.foes
        
    @smart_defaults(*CopyContextDefaults)
    def copy(self, parent=None, event=None, foes=None):
        """ Copy the Context """
        return PlayerContext(self.game, parent, event=event, player=self.player, foes=GetPlayerFoes(self.player, self.potentialPlayers))
        
    @smart_defaults(*CopyContextDefaults)
    def getPlayerContext(self, player, parent=None, event=None, foes=None):
        """ Get the Context for the given player """
        return PlayerContext(self.game, parent, event=event, player=player, foes=GetPlayerFoes(player, self.potentialPlayers))
