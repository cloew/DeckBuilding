
class PlayerResults:
    """ Represents player results """
    
    def __init__(self, player, game):
        """ Initialize the Player Results """
        self.player = player
        self.points = self.player.calculatePoints(game)