from Game.Effects.effect_runner import PerformEffects

class Activatable:
    """ Represents an effect that can be activated """
    
    def __init__(self, effects, singleUse=False):
        """ Initialize the Activatable Effect """
        self.effects = effects
        self.singleUse = singleUse
        
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