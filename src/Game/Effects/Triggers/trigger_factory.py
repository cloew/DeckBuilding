from Game.Effects.Triggers.trigger import Trigger

from Game.Effects.effect_factory import EffectFactory

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
        effect = EffectFactory.loadEffect(triggerJson["effect"])
        return Trigger(eventType, effect)
        
TriggerFactory = TriggerFactory()