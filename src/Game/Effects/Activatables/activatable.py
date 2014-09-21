from Game.Effects.effect_arguments import EffectArguments
from Game.Effects.effect_runner import PerformEffects

class Activatable:
    """ Represents an effect that can be activated """
    
    def __init__(self, effects, condition=None, singleUse=False):
        """ Initialize the Activatable Effect """
        self.effects = effects
        self.condition = condition
        self.singleUse = singleUse
        
    def canActivate(self, game):
        """ Return if the Activatable can activate """
        args = EffectArguments(game, None)
        return self.condition is None or self.condition.evaluate(args)
        
    def activate(self, args):
        """ Activate the effect """
        coroutine = PerformEffects(self.effects, args)
        try:
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response)
        except StopIteration:
            pass
        
        if self.singleUse:
            args.owner.unregisterActivatable(args.parent)