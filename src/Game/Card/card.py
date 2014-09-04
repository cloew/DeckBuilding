
class Card:
    """ Represents a Card in the Deck Building Game """
    
    def __init__(self):
        """ Initialize the Card """
        self.name = None
        self.costCalculator = None
        self.victoryPointsCalculator = None
        
        self.playEffects = None
        self.availableEffects = None
        self.triggerableEffects = None