from Game.Effects.add_trigger import AddTrigger
from Game.Effects.attack import Attack
from Game.Effects.choice import Choice, Option
from Game.Effects.conditional_effect import ConditionalEffect
from Game.Effects.destroy import Destroy
from Game.Effects.discard import Discard
from Game.Effects.draw import Draw
from Game.Effects.gain_card import GainCard
from Game.Effects.gain_power import GainPower
from Game.Effects.look_at_top import LookAtTop
from Game.Effects.modify_hand_size import ModifyHandSize
from Game.Effects.move_card import MoveCard
from Game.Effects.ongoing import Ongoing
from Game.Effects.per_match import PerMatch
from Game.Effects.pick_cards import PickCards
from Game.Effects.pick_random_card import PickRandomCard
from Game.Effects.play import Play
from Game.Effects.play_or_have_played import PlayOrHavePlayed
from Game.Effects.put_on_bottom_cleanup import PutOnBottomCleanup
from Game.Effects.spend_power import SpendPower

from Game.Effects.Conditions.condition_factory import ConditionFactory
from Game.Effects.Conditions.Filters.filter_factory import FilterFactory
from Game.Effects.Conditions.Filters.Criteria.criteria_factory import CriteriaFactory


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
        elif effectType == "ATTACK":
            effect = EffectFactory.loadEffect(effectJson["effect"])
            return Attack(effect)
        elif effectType == "CHOICE":
            options = [Option(optionJSON['description'], self.loadEffects(optionJSON['effects'])) for optionJSON in effectJson['choices']]
            relevantSourceType = None
            if "source" in effectJson:
                relevantSourceType = effectJson["source"]
            return Choice(options, relevantSourceType=relevantSourceType)
        elif effectType == "CONDITIONAL":
            condition = ConditionFactory.loadCondition(effectJson["condition"])
            effect = EffectFactory.loadEffect(effectJson["effect"])
            otherwiseEffect = None
            if "otherwise" in effectJson:
                otherwiseEffect = EffectFactory.loadEffect(effectJson["otherwise"])
            return ConditionalEffect(condition, effect, otherwiseEffect=otherwiseEffect)
        elif effectType == "DESTROY":
            return Destroy(effectJson["source"])
        elif effectType == "DISCARD":
            return Discard(effectJson["source"])
        elif effectType == "DRAW":
            return Draw(effectJson["count"])
        elif effectType == "GAIN_CARD":
            toSource = None
            if "to" in effectJson:
                toSource = effectJson["to"]
            return GainCard(effectJson["from"], toSourceType=toSource)
        elif effectType == "GAIN_POWER":
            return GainPower(effectJson["power"])
        elif effectType == "LOOK_AT_TOP":
            return LookAtTop(effectJson["source"], self.loadEffect(effectJson["then"]))
        elif effectType == "MOD_HAND_SIZE":
            return ModifyHandSize(effectJson["change"])
        elif effectType == "MOVE_CARD":
            return MoveCard(effectJson["from"], effectJson["to"])
        elif effectType == "ONGOING":
            return Ongoing()
        elif effectType == "PER_MATCH":
            criteria = CriteriaFactory.loadCriteria(effectJson["criteria"])
            effect = EffectFactory.loadEffect(effectJson["effect"])
            return PerMatch(effectJson["sourceType"], criteria, effect)
        elif effectType == "PICK_CARDS":
            filter = None
            if "criteria" in effectJson:
                filterJson = {"criteria":effectJson["criteria"]}
                filterJson["sourceType"] = effectJson["source"]
                filterJson["type"] = "COMPARISON"
                filter = FilterFactory.loadFilter(filterJson)
            return PickCards(effectJson["source"], effectJson["number"], self.loadEffect(effectJson["then"]), filter=filter)
        elif effectType == "PICK_RANDOM":
            return PickRandomCard(effectJson["source"], self.loadEffect(effectJson["then"]))
        elif effectType == "PLAY":
            remove = None
            if "remove" in effectJson:
                remove = effectJson["remove"]
            return Play(effectJson["source"], remove=remove)
        elif effectType == "PLAY_OR_HAVE_PLAYED":
            criteria = CriteriaFactory.loadCriteria(effectJson["criteria"])
            effect = EffectFactory.loadEffect(effectJson["effect"])
            return PlayOrHavePlayed(effect, criteria)
        elif effectType == "PUT_ON_BOTTOM":
            return PutOnBottomCleanup()
        elif effectType == "SPEND_POWER":
            return SpendPower(effectJson["power"])
        return None
        
EffectFactory = EffectFactory()