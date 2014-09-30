from Game.Effects.effect_arguments import EffectArguments
from Game.Effects.effect_runner import PerformEffects

class Card:
    """ Represents a Card in the Deck Building Game """
    
    def __init__(self, name, cardType, costCalculator=None, vpCalculator=None, playEffects=[], onGainEffects=[],
                       defenseEffects=[], appearanceEffects=[], triggers=[], activatable=None, image=None):
        """ Initialize the Card """
        self.name = name
        self.cardType = cardType
        
        self.costCalculator = costCalculator
        self.calculateCost = self.costCalculator.calculateCost
        self.victoryPointsCalculator = vpCalculator
        self.calculatePoints = self.victoryPointsCalculator.calculatePoints
        
        self.playEffects = playEffects
        self.onGainEffects = onGainEffects
        self.defenseEffects = defenseEffects
        self.appearanceEffects = appearanceEffects
        self.activatableEffect = activatable
        self.triggerEffects = triggers
        
        if image is None:
            image = "vulnerability.jpg"
        self.image = image
        
    def play(self, game):
        """ Play the card and perform any effects """
        args = EffectArguments(game, self)
        coroutine = PerformEffects(self.playEffects, args)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)
            
    @property
    def cost(self):
        """ Return the cost of the Card """
        return self.calculateCost()
        
    @property
    def isDefense(self):
        """ Return if the Card is a defense """
        return len(self.defenseEffects) > 0
        
    def __repr__(self):
        """ Return the String Representation of the card """
        return "{0}:{1}".format(self.name, self.calculateCost())