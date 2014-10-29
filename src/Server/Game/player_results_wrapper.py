
class PlayerResultsWrapper:
    """ A Wrapper for a Player's Game Results """
    
    def __init__(self, player, isYou):
        """ Initialize the Player Wrapper """
        self.player = player
        self.isYou = isYou
        
    def toJSON(self, game):
        """ Return the Player as a JSON Dictionary """
        return {'points':self.player.calculatePoints(game), 'name':self.player.name, 'isYou':self.isYou}