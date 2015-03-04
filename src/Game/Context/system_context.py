from context import Context
from player_context import PlayerContext, GetPlayerFoes

from Game.player_order_helper import GetPlayersStartingWith

from smart_defaults import smart_defaults, ViaField

class SystemContext(Context):
    """ Represents the game context for the System to use """
    
    def __init__(self, game, parent, event=None, foes=None):
        """ Initialize the Arguments """
        Context.__init__(self, game, parent, event=event)
        self.player = None
        if foes is None:
            foes = self._foes
        self.foes = foes
        
    @property
    def _foes(self):
        """ Return the foes of the current player """
        return GetPlayersStartingWith(self.owner.player, self.game.players)
        
    @smart_defaults
    def copy(self, parent=ViaField("parent"), event=ViaField("event"), foes=ViaField("foes")):
        """ Copy the Context """
        return SystemContext(self.game, parent, event=event, foes=foes)
        
    @smart_defaults
    def getPlayerContext(self, player, parent=ViaField("parent"), event=ViaField("event"), foes=ViaField("foes")):
        """ Get the Context for the given player """
        return PlayerContext(self.game, parent, event=event, player=player, foes=GetPlayerFoes(player, foes))