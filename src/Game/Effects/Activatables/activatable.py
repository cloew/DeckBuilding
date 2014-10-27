from Game.Effects.game_contexts import PlayerContext
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
        context = PlayerContext(game, None)
        return self.condition is None or self.condition.evaluate(context)
        
    def activate(self, context):
        """ Activate the effect """
        if self.singleUse:
            context.owner.unregisterActivatable(context.parent, self)
        
        coroutine = PerformEffects(self.effects, context)
        try:
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response)
        except StopIteration:
            pass