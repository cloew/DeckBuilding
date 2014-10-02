
class EnoughPower:
    """ Represents a condition to check if a player has enough power """
    
    def __init__(self, power):
        """ Initialize the Enough Power COndition with the amount of power needed """
        self.power = power
        
    def evaluate(self, context):
        """ Evaluate the condition """
        return context.owner.power >= self.power