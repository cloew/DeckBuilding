from context import Context

from Game.player_order_helper import GetPlayersStartingWith, GetNextPlayer, GetPreviousPlayer

from smart_defaults import smart_defaults, ViaField

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
        return self.getPotentialPlayers(self.foes)
        
    def getPotentialPlayers(self, foes):
        """ Return the players available in the current context """
        return [self.player] + foes
        
    @smart_defaults
    def copy(self, parent=ViaField("parent"), event=ViaField("event"), foes=ViaField("foes")):
        """ Copy the Context """
        return PlayerContext(self.game, parent, event=event, player=self.player, foes=GetPlayerFoes(self.player, self.getPotentialPlayers(foes)))
        
    @smart_defaults
    def getPlayerContext(self, player, parent=ViaField("parent"), event=ViaField("event"), foes=ViaField("foes")):
        """ Get the Context for the given player """
        return PlayerContext(self.game, parent, event=event, player=player, foes=GetPlayerFoes(player, self.getPotentialPlayers(foes)))
