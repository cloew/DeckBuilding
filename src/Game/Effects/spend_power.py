
class SpendPower:
    """ Represents an effect to spend power this turn """
    
    def __init__(self, power):
        """ Initialize the Effect with the power to spend """
        self.power = power
        
    def perform(self, args):
        """ Perform the Game Effect """
        args.owner.spendPower(self.power)