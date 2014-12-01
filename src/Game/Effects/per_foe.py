from Game.Effects.effect_runner import PerformEffectsForEachPlayer

class PerFoe:
    """ Represents an effect to perform for each foe """
    
    def __init__(self, effects):
        """ Initialize the Effect with the effect to attack with """
        self.effects = effects
        
    def perform(self, context):
        """ Perform the Game Effect """
        self.failedEffects = []
        coroutine = PerformEffectsForEachPlayer(self.effects, context.foes, context, self.failedEffects)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)