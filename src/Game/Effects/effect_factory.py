from Game.Effects.draw import Draw
from Game.Effects.gain_power import GainPower
from Game.Effects.ongoing import Ongoing

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
        
        if effectType == "DRAW":
            return Draw(effectJson["count"])
        elif effectType == "GAIN_POWER":
            return GainPower(effectJson["power"])
        elif effectType == "ONGOING":
            return Ongoing()
        return None
        
EffectFactory = EffectFactory()