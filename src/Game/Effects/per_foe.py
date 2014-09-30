from Game.Effects.effect_runner import PerformEffects

class PerFoe:
    """ Represents an effect to perform for each foe """
    
    def __init__(self, effects):
        """ Initialize the Effect with the effect to attack with """
        self.effects = effects
        
    def perform(self, args):
        """ Perform the Game Effect """
        coroutine = PerformEffectsForEachPlayer(self.effects, args.foes, args)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)