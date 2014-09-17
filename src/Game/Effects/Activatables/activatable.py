from Game.Effects.effect_runner import PerformEffect

class Activatable:
    """ Represents an effect that can be activated """
    
    def __init__(self, effect, singleUse=False):
        """ Initialize the Activatable Effect """
        self.effect = effect
        self.singleUse = singleUse
        
    def activate(self, args):
        """ Activate the effect """
        coroutine = PerformEffect(self.effect, args)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)
        
        if self.singleUse:
            args.owner.unregisterActivatable(args.parent)