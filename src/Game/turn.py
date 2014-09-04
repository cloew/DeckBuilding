
class Turn:
    """ Represents a turn in the game """
    
    def __init__(self, player):
        """ Initialize the Turn """
        self.player = player
        self.power = 0
        
    def gainPower(self, power):
        """ Gain the appropriate amount of power """
        self.power += power