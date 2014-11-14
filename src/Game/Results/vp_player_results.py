from player_results import PlayerResults

class VPPlayerResults(PlayerResults):
    """ Represents player results based on victory points """
    PRIORITY = 0
    
    def __init__(self, player, game):
        """ Initialize the Player Results """
        self.player = player
        self.points = self.player.calculatePoints(game)