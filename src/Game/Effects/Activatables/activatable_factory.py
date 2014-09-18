from Game.Effects.Activatables.activatable import Activatable

from Game.Effects.effect_factory import EffectFactory
from Game.Effects.Conditions.condition_factory import ConditionFactory

class ActivatableFactory:
    """ Factory to construct Activatables """
    
    def loadActivatable(self, activatableJson):
        """ Load the trigger in the given JSON """
        singleUse = activatableJson["singleUse"]
        condition = None
        if "condition" in activatableJson:
            condition = ConditionFactory.loadCondition(activatableJson["condition"])
        effects = EffectFactory.loadEffects(activatableJson["effects"])
        return Activatable(effects, condition=condition, singleUse=singleUse)
        
ActivatableFactory = ActivatableFactory()