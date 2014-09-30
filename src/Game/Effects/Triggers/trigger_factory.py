from Game.Effects.Triggers.trigger import Trigger

from Game.Effects.effect_factory import EffectFactory
from Game.Effects.Conditions.condition_factory import ConditionFactory

class TriggerFactory:
    """ Factory to create Trigger Effects """
    
    def loadTriggers(self, triggersJson):
        """ Load the triggers in the given JSON """
        triggers = []
        for triggerJson in triggersJson:
            triggers.append(self.loadTrigger(triggerJson))
        return triggers
        
    def loadTrigger(self, triggerJson):
        """ Load the trigger in the given JSON """
        eventType = triggerJson["type"]
        singleUse = triggerJson["singleUse"]
        condition = ConditionFactory.load(triggerJson["condition"])
        effect = EffectFactory.load(triggerJson["effect"])
        return Trigger(eventType, condition, effect, singleUse=singleUse)
        
TriggerFactory = TriggerFactory()