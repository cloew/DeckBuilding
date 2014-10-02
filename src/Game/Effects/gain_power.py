
class GainPower:
    """ Represents an effect that gains power for the playing player """
    
    def __init__(self, power):
        """ Initialize the Effect with the power to gain """
        self.power = power
        
    def perform(self, context):
        """ Perform the Game Effect """
        context.owner.gainPower(context.parent, self.power)
        # Will probably return some kind of message object that says power was gained and by what