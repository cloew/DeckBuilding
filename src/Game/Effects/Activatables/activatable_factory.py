from Game.Effects.Activatables.activatable import Activatable

from Game.Effects.effect_factory import EffectFactory
from Game.Effects.Conditions.condition_factory import ConditionFactory

class ActivatableFactory:
    """ Factory to construct Activatables """
    
    def loadActivatable(self, activatableJson):
        """ Load the trigger in the given JSON """
        singleUse = activatableJson["singleUse"]
        # condition = ConditionFactory.loadCondition(triggerJson["condition"])
        effect = EffectFactory.loadEffect(activatableJson["effect"])
        return Activatable(effect, singleUse=singleUse)
        
ActivatableFactory = ActivatableFactory()