
class PowerTracker:
    """ Represents the Power Generated during a turn """
    
    def __init__(self):
        """ Initialize the Power Tracker """
        self.cardToPower = {}
        self.spentPower = 0
        self.modifier = 1
        
    def gainPower(self, card, power):
        """ Gain Power from the given card """
        print "Gaining Power:", power
        if card in self.cardToPower:
            self.cardToPower[card] += power
        else:
            self.cardToPower[card] = power
            
    def spendPower(self, power):
        """ Spend the given amount of power """
        self.spentPower += power
       
    @property
    def power(self):
        """ Return the current power level for the turn """
        print "Gained Power:", sum(self.cardToPower.values())
        print "Times Modifier:", sum(self.cardToPower.values())*self.modifier
        print "Minus Spent Power:", sum(self.cardToPower.values())*self.modifier - self.spentPower
        return sum(self.cardToPower.values())*self.modifier - self.spentPower