from player_results import PlayerResults
from vp_player_results import VPPlayerResults

class EffectPlayerResults(PlayerResults):
    """ Represents player results based on winning from an effect """
    PRIORITY = 1
    
    def __init__(self, player, game):
        """ Initialize the Player Results """
        self.player = player
        self.vpResults = VPPlayerResults(player, game)
        
    @property
    def points(self):
        """ Return the points """
        return self.vpResults.points