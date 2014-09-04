
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
        
    def play(self, owner):
        """ Play the card and perform any effects """
        for effect in self.playEffects:
            effect.perform(owner)
        
    def __repr__(self):
        """ Return the String Representation of the card """
        return self.name