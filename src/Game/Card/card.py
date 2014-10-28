from Game.Effects.game_contexts import PlayerContext
from Game.Effects.effect_runner import PerformEffects

class Card:
    """ Represents a Card in the Deck Building Game """
    
    def __init__(self, name, cardType, costCalculator=None, vpCalculator=None, playEffects=[], onGainEffects=[],
                       defenseEffects=[], defendFrom=None, appearanceEffects=[], triggers=[], activatable=None, image=None):
        """ Initialize the Card """
        self.name = name
        self.cardType = cardType
        
        self.costCalculator = costCalculator
        self.calculateCost = self.costCalculator.calculateCost
        self.addCostModifier = self.costCalculator.addCostModifier
        self.removeCostModifier = self.costCalculator.removeCostModifier
        
        self.victoryPointsCalculator = vpCalculator
        self.calculatePoints = self.victoryPointsCalculator.calculatePoints
        
        self.playEffects = playEffects
        self.onGainEffects = onGainEffects
        self.defenseEffects = defenseEffects
        self.defendFrom = defendFrom
        self.appearanceEffects = appearanceEffects
        self.activatableEffect = activatable
        self.triggerEffects = triggers
        
        if image is None:
            image = "vulnerability.jpg"
        self.image = image
        
        for trigger in triggers:
            trigger.parent = self
        
    def play(self, game, effectTypesToIgnore=[]):
        """ Play the card and perform any effects """
        context = PlayerContext(game, self)
        coroutine = PerformEffects(self.playEffects, context, effectTypesToIgnore=effectTypesToIgnore)
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