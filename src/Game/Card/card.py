
class Card:
    """ Represents a Card in the Deck Building Game """
    
    def __init__(self, name, playEffects=[]):
        """ Initialize the Card """
        self.name = name
        self.costCalculator = None
        self.victoryPointsCalculator = None
        
        self.playEffects = playEffects
        self.activatableEffects = None
        self.triggerableEffects = None