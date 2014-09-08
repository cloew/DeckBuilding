from Game.Effects.conditional_effect import ConditionalEffect
from Game.Effects.draw import Draw
from Game.Effects.gain_power import GainPower
from Game.Effects.ongoing import Ongoing
from Game.Effects.per_match import PerMatch

from Game.Effects.Conditions.condition_factory import ConditionFactory

class EffectFactory:
    """ Factory to create Game Effects """
    
    def loadEffects(self, effectsJson):
        """ Load the effects in the given JSON """
        effects = []
        for effectJson in effectsJson:
            effects.append(self.loadEffect(effectJson))
        return effects
        
    def loadEffect(self, effectJson):
        """ Load the effect in the given JSON """
        effectType = effectJson['type']
        
        if effectType == "CONDITIONAL":
            condition = ConditionFactory.loadCondition(effectJson["condition"])
            effect = EffectFactory.loadEffect(effectJson["effect"])
            return ConditionalEffect(condition, effect)
        elif effectType == "DRAW":
            return Draw(effectJson["count"])
        elif effectType == "GAIN_POWER":
            return GainPower(effectJson["power"])
        elif effectType == "ONGOING":
            return Ongoing()
        elif effectType == "PER_MATCH":
            effect = EffectFactory.loadEffect(effectJson["effect"])
            return PerMatch(effectJson["field"], effectJson["values"], effectJson["sourceType"], effect)
        return None
        
EffectFactory = EffectFactory()