from Game.Effects.add_trigger import AddTrigger
from Game.Effects.choice import Choice, Option
from Game.Effects.conditional_effect import ConditionalEffect
from Game.Effects.destroy import Destroy
from Game.Effects.discard import Discard
from Game.Effects.draw import Draw
from Game.Effects.gain_card import GainCard
from Game.Effects.gain_power import GainPower
from Game.Effects.look_at_top import LookAtTop
from Game.Effects.move_card import MoveCard
from Game.Effects.ongoing import Ongoing
from Game.Effects.per_match import PerMatch

from Game.Effects.Conditions.condition_factory import ConditionFactory
from Game.Effects.Conditions.filter import Filter

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
        
        if effectType == "ADD_TRIGGER":
            from Game.Effects.Triggers.trigger_factory import TriggerFactory
            return AddTrigger(TriggerFactory.loadTrigger(effectJson["trigger"]))
        elif effectType == "CHOICE":
            options = [Option(optionJSON['description'], self.loadEffects(optionJSON['effects'])) for optionJSON in effectJson['choices']]
            return Choice(options)
        elif effectType == "CONDITIONAL":
            condition = ConditionFactory.loadCondition(effectJson["condition"])
            effect = EffectFactory.loadEffect(effectJson["effect"])
            return ConditionalEffect(condition, effect)
        elif effectType == "DESTROY":
            return Destroy()
        elif effectType == "DISCARD":
            return Discard(effectJson["source"])
        elif effectType == "DRAW":
            return Draw(effectJson["count"])
        elif effectType == "GAIN_CARD":
            return GainCard()
        elif effectType == "GAIN_POWER":
            return GainPower(effectJson["power"])
        elif effectType == "LOOK_AT_TOP":
            return LookAtTop(effectJson["source"], self.loadEffect(effectJson["then"]))
        elif effectType == "MOVE_CARD":
            filter = None
            if "filter" in effectJson:
                filterJson = effectJson["filter"]
                filter = Filter(filterJson["field"], filterJson["values"], effectJson["from"])
            
            return MoveCard(effectJson["from"], effectJson["to"], filter=filter)
        elif effectType == "ONGOING":
            return Ongoing()
        elif effectType == "PER_MATCH":
            effect = EffectFactory.loadEffect(effectJson["effect"])
            return PerMatch(effectJson["field"], effectJson["values"], effectJson["sourceType"], effect)
        return None
        
EffectFactory = EffectFactory()