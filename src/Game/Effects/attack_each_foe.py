from Game.Effects.attack import Attack
from Game.Effects.per_foe import PerFoe

from Game.Effects.effect_runner import PerformEffects

class AttackEachFoe(Attack):
    """ Represents an effect to Attack other Players """
    
    def __init__(self, effects, anyFailedEffects=[]):
        """ Initialize with the effects to attack each foe with """
        self.perFoeEffect = PerFoe(effects)
        Attack.__init__(self, [self.perFoeEffect])
        self.anyFailedEffects = anyFailedEffects
        
    def perform(self, context):
        """ Perform the Game Effect """
        coroutine = Attack.perform(self, context)
        try:
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response)
        except StopIteration:
            pass
        
        self.failedAttacks += self.perFoeEffect.failedEffects
        if any(self.failedAttacks):
            coroutine = PerformEffects(self.anyFailedEffects, context)
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response)