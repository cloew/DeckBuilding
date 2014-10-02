
class SpendPower:
    """ Represents an effect to spend power this turn """
    
    def __init__(self, power):
        """ Initialize the Effect with the power to spend """
        self.power = power
        
    def perform(self, context):
        """ Perform the Game Effect """
        context.owner.spendPower(self.power)