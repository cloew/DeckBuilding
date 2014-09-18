
class EnoughPower:
    """ Represents a condition to check if a player has enough power """
    
    def __init__(self, power):
        """ Initialize the Enough Power COndition with the amount of power needed """
        self.power = power
        
    def evaluate(self, game, event=None):
        """ Evaluate the condition """
        return game.currentTurn.power >= self.power