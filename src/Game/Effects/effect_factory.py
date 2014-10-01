from Game.Effects.activate_character import ActivateCharacter
from Game.Effects.add_to_line_up import AddToLineUp
from Game.Effects.add_trigger import AddTrigger
from Game.Effects.attack import Attack
from Game.Effects.change_power_modifier import ChangePowerModifier
from Game.Effects.choice import Choice, Option
from Game.Effects.conditional_effect import ConditionalEffect
from Game.Effects.deactivate_character import DeactivateCharacter
from Game.Effects.destroy import Destroy
from Game.Effects.discard import Discard
from Game.Effects.draw import Draw
from Game.Effects.filter import Filter
from Game.Effects.gain_card import GainCard
from Game.Effects.gain_power import GainPower
from Game.Effects.gain_top_card import GainTopCard
from Game.Effects.look_at_top import LookAtTop
from Game.Effects.modify_hand_size import ModifyHandSize
from Game.Effects.move_card import MoveCard
from Game.Effects.ongoing import Ongoing
from Game.Effects.per_foe import PerFoe
from Game.Effects.per_match import PerMatch
from Game.Effects.pick_cards import PickCards
from Game.Effects.pick_random_card import PickRandomCard
from Game.Effects.pick_up_to_all_cards import PickUpToAllCards
from Game.Effects.pick_up_to_n_cards import PickUpToNCards
from Game.Effects.play import Play
from Game.Effects.play_or_have_played import PlayOrHavePlayed
from Game.Effects.put_on_bottom import PutOnBottom
from Game.Effects.put_on_bottom_cleanup import PutOnBottomCleanup
from Game.Effects.spend_power import SpendPower

from Game.Effects.Conditions.condition_factory import ConditionFactory
from Game.Effects.Conditions.Filters.filter_factory import FilterFactory
from Game.Effects.Conditions.Filters.Criteria.criteria_factory import CriteriaFactory

from Game.Factory.comparison_filter_parameter import ComparisonFilterParameter
from Game.Factory.filter_parameter import FilterParameter

from kao_factory.factory import Factory
from kao_factory.typed_factory import TypedFactory
from kao_factory.Parameter.complex_parameter import ComplexParameter
from kao_factory.Parameter.primitive_parameter import PrimitiveParameter
        
def LoadTrigger(data):
    """ Load a trigger from the data given """
    from Game.Effects.Triggers.trigger_factory import TriggerFactory
    return TriggerFactory.load(data)
    
def LoadOptions(data):
    """ Load options from the data given """
    return [Option(optionJSON['description'], EffectFactory.loadAll(optionJSON['effects'])) for optionJSON in data]

EffectFactory = TypedFactory('type', {"ACTIVATE_CHARACTER":Factory(ActivateCharacter, []),
                                      "ADD_TO_LINE_UP":Factory(AddToLineUp, [PrimitiveParameter("count", optional=True)]),
                                      "ADD_TRIGGER":Factory(AddTrigger, [PrimitiveParameter("power")]),
                                      "CHOICE":Factory(Choice, [ComplexParameter("choices", LoadOptions), PrimitiveParameter("source")]),
                                      "DEACTIVATE_CHARACTER":Factory(DeactivateCharacter, []),
                                      "DESTROY":Factory(Destroy, [PrimitiveParameter("source")]),
                                      "DISCARD":Factory(Discard, [PrimitiveParameter("source")]),
                                      "DRAW":Factory(Draw, [PrimitiveParameter("count")]),
                                      "GAIN_CARD":Factory(GainCard, [PrimitiveParameter("from"), PrimitiveParameter("to", optional=True)]),
                                      "GAIN_POWER":Factory(GainPower, [PrimitiveParameter("power")]),
                                      "GAIN_TOP_CARD":Factory(GainTopCard, [PrimitiveParameter("from"), PrimitiveParameter("to", optional=True)]),
                                      "MOD_HAND_SIZE":Factory(ModifyHandSize, [PrimitiveParameter("change")]),
                                      "MOVE_CARD":Factory(MoveCard, [PrimitiveParameter("from"), PrimitiveParameter("to")]),
                                      "ONGOING":Factory(Ongoing, []),
                                      "PLAY":Factory(Play, [PrimitiveParameter("source"), PrimitiveParameter("remove", optional=True)]),
                                      "POWER_MOD":Factory(ChangePowerModifier, [PrimitiveParameter("modifier")]),
                                      "PUT_ON_BOTTOM":Factory(PutOnBottom, [PrimitiveParameter("from"), PrimitiveParameter("to")]),
                                      "PUT_ON_BOTTOM_CLEANUP":Factory(PutOnBottomCleanup, []),
                                      "SPEND_POWER":Factory(SpendPower, [PrimitiveParameter("power")])})
                                      
EffectFactory.addFactory("ATTACK", Factory(Attack, [ComplexParameter("effect", EffectFactory.load)]))
EffectFactory.addFactory("CONDITIONAL", Factory(ConditionalEffect, [ComplexParameter("condition", ConditionFactory.load), 
                                                                    ComplexParameter("effect", EffectFactory.load), 
                                                                    ComplexParameter("otherwise", EffectFactory.load, optional=True)]))
EffectFactory.addFactory("FILTER", Factory(Filter, [PrimitiveParameter("source"), FilterParameter(), ComplexParameter("then", EffectFactory.loadAll)]))
EffectFactory.addFactory("LOOK_AT_TOP", Factory(LookAtTop, [PrimitiveParameter("source"), ComplexParameter("then", EffectFactory.load)]))
EffectFactory.addFactory("PER_FOE", Factory(PerFoe, [ComplexParameter("effects", EffectFactory.loadAll)]))
EffectFactory.addFactory("PER_MATCH", Factory(PerMatch, [PrimitiveParameter("source"), ComplexParameter("effect", EffectFactory.load), FilterParameter(optional=True)]))
EffectFactory.addFactory("PICK_CARDS", Factory(PickCards, [PrimitiveParameter("source"), PrimitiveParameter("number"), 
                                                           ComplexParameter("then", EffectFactory.loadAll), ComparisonFilterParameter(optional=True)]))
EffectFactory.addFactory("PICK_RANDOM", Factory(PickRandomCard, [PrimitiveParameter("source"), ComplexParameter("then", EffectFactory.load)]))
EffectFactory.addFactory("PICK_UP_TO_ALL_CARDS", Factory(PickUpToAllCards, [PrimitiveParameter("source"), ComplexParameter("then", EffectFactory.loadAll), 
                                                                            ComparisonFilterParameter(optional=True)]))
EffectFactory.addFactory("PICK_UP_TO_N_CARDS", Factory(PickUpToNCards, [PrimitiveParameter("source"), PrimitiveParameter("number"), 
                                                                        ComplexParameter("then", EffectFactory.loadAll), ComparisonFilterParameter(optional=True)]))
EffectFactory.addFactory("PLAY_OR_HAVE_PLAYED", Factory(PlayOrHavePlayed, [ComplexParameter("effect", EffectFactory.load), ComplexParameter("criteria", CriteriaFactory.load)]))