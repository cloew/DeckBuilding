from Game.Effects.effect_arguments import EffectArguments

class Card:
    """ Represents a Card in the Deck Building Game """
    
    def __init__(self, name, cardType, costCalculator=None, playEffects=[], triggers=[],image=None):
        """ Initialize the Card """
        self.name = name
        self.cardType = cardType
        
        self.costCalculator = costCalculator
        self.calculateCost = self.costCalculator.calculateCost
        
        self.victoryPointsCalculator = None
        
        self.playEffects = playEffects
        self.activatableEffects = None
        self.triggerEffects = triggers
        
        if image is None:
            image = "vulnerability.jpg"
        self.image = image
        
    def play(self, game):
        """ Play the card and perform any effects """
        args = EffectArguments(game, self)
        for effect in self.playEffects:
            effect.perform(args)
        
    def __repr__(self):
        """ Return the String Representation of the card """
        return "{0}:{1}".format(self.name, self.calculateCost())