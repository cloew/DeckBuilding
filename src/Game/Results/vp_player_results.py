
class VPPlayerResults:
    """ Represents player results based on victory points """
    
    def __init__(self, player, game):
        """ Initialize the Player Results """
        self.player = player
        self.points = self.player.calculatePoints(game)