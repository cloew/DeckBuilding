from Game.Effects.effect_runner import PerformEffects

class PerFoe:
    """ Represents an effect to perform for each foe """
    
    def __init__(self, effects):
        """ Initialize the Effect with the effect to attack with """
        self.effects = effects
        
    def perform(self, args):
        """ Perform the Game Effect """
        foes = args.foes
        for foe in args.foes:
            args = args.copy()
            args.player = foe
            
            coroutine = PerformEffects(self.effects, args)
            try:
                response = yield coroutine.next()
                while True:
                    response = yield coroutine.send(response)
            except StopIteration:
                pass