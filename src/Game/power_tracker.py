
class PowerTracker:
    """ Represents the Power Generated during a turn """
    
    def __init__(self):
        """ Initialize the Power Tracker """
        self.cardToPower = {}
        self.spentPower = 0
        self.modifier = 1
        
    def gainPower(self, card, power):
        """ Gain Power from the given card """
        if card in self.cardToPower:
            self.cardToPower[card] += power
        else:
            self.cardToPower[card] = power
            
    def spendPower(self, power):
        """ Spend the given amount of power """
        self.spentPower += power
        
    def changeModifier(self, modifier):
        """ Change the Modifier by the given modifier """
        self.modifier *= modifier
       
    @property
    def power(self):
        """ Return the current power level for the turn """
        return sum(self.cardToPower.values())*self.modifier - self.spentPower