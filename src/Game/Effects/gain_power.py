
class GainPower:
    """ Represents an effect that gains power for the playing player """
    
    def __init__(self, power):
        """ Initialize the Effect with the power to gain """
        self.power = power
        
    def perform(self, args):
        """ Perform the Game Effect """
        args.owner.gainPower(args.parent, self.power)
        # Will probably return some kind of message object that says power was gained and by what