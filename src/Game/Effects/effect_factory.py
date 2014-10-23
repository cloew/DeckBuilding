from Game.Card.Cost.fixed_cost import FixedCost

from Game.Effects.activate_character import ActivateCharacter
from Game.Effects.add_activatable import AddActivatable
from Game.Effects.add_cost_modifier import AddCostModifier
from Game.Effects.add_to_line_up import AddToLineUp
from Game.Effects.add_trigger import AddTrigger
from Game.Effects.as_next_player import AsNextPlayer
from Game.Effects.as_player_with_highest_cost import AsPlayerWithHighestCost
from Game.Effects.as_only_player_with_highest_cost import AsOnlyPlayerWithHighestCost
from Game.Effects.as_previous_player import AsPreviousPlayer
from Game.Effects.as_owner import AsOwner
from Game.Effects.attack import Attack
from Game.Effects.attack_each_foe import AttackEachFoe
from Game.Effects.change_power_modifier import ChangePowerModifier
from Game.Effects.choice import Choice, Option
from Game.Effects.collect_cards import CollectCards
from Game.Effects.conditional_effect import ConditionalEffect
from Game.Effects.deactivate_character import DeactivateCharacter
from Game.Effects.destroy import Destroy
from Game.Effects.discard import Discard
from Game.Effects.draw import Draw
from Game.Effects.draw_until import DrawUntil
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
from Game.Effects.play_or_have_played_another import PlayOrHavePlayedAnother
from Game.Effects.put_on_bottom import PutOnBottom
from Game.Effects.put_on_bottom_cleanup import PutOnBottomCleanup
from Game.Effects.reveal import Reveal
from Game.Effects.shuffle_and_deal import ShuffleAndDeal
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

        
def LoadActivatable(data):
    """ Load an activatable from the data given """
    from Game.Effects.Activatables.activatable_factory import ActivatableFactory
    return ActivatableFactory.load(data)
    
def LoadCost(data):
    """ Load the Cost """
    return FixedCost(data["cost"], canBeNegative=True)
    
def LoadTrigger(data):
    """ Load a trigger from the data given """
    from Game.Effects.Triggers.trigger_factory import TriggerFactory
    return TriggerFactory.load(data)

EffectFactory = TypedFactory('type', {"ACTIVATE_CHARACTER":Factory(ActivateCharacter, []),
                                      "ADD_ACTIVATABLE":Factory(AddActivatable, [ComplexParameter("activatable", LoadActivatable)]),
                                      "ADD_COST_MOD":Factory(AddCostModifier, [PrimitiveParameter("source"), ComplexParameter("cost", LoadCost)]),
                                      "ADD_TO_LINE_UP":Factory(AddToLineUp, [PrimitiveParameter("count", optional=True)]),
                                      "ADD_TRIGGER":Factory(AddTrigger, [ComplexParameter("trigger", LoadTrigger)]),
                                      "DEACTIVATE_CHARACTER":Factory(DeactivateCharacter, []),
                                      "DESTROY":Factory(Destroy, [PrimitiveParameter("source")]),
                                      "DISCARD":Factory(Discard, [PrimitiveParameter("source")]),
                                      "DRAW":Factory(Draw, [PrimitiveParameter("count")]),
                                      "DRAW_UNTIL":Factory(DrawUntil, [PrimitiveParameter("cost")]),
                                      "GAIN_CARD":Factory(GainCard, [PrimitiveParameter("from"), PrimitiveParameter("to", optional=True)]),
                                      "GAIN_POWER":Factory(GainPower, [PrimitiveParameter("power")]),
                                      "GAIN_TOP_CARD":Factory(GainTopCard, [PrimitiveParameter("from"), PrimitiveParameter("to", optional=True)]),
                                      "MOD_HAND_SIZE":Factory(ModifyHandSize, [PrimitiveParameter("change")]),
                                      "MOVE_CARD":Factory(MoveCard, [PrimitiveParameter("from"), PrimitiveParameter("to")]),
                                      "ONGOING":Factory(Ongoing, []),
                                      "PLAY":Factory(Play, [PrimitiveParameter("source"), PrimitiveParameter("returnTo", optional=True)]),
                                      "POWER_MOD":Factory(ChangePowerModifier, [PrimitiveParameter("modifier")]),
                                      "PUT_ON_BOTTOM":Factory(PutOnBottom, [PrimitiveParameter("from"), PrimitiveParameter("to")]),
                                      "PUT_ON_BOTTOM_CLEANUP":Factory(PutOnBottomCleanup, []),
                                      "REVEAL":Factory(Reveal, [PrimitiveParameter("source")]),
                                      "SHUFFLE_AND_DEAL":Factory(ShuffleAndDeal, []),
                                      "SPEND_POWER":Factory(SpendPower, [PrimitiveParameter("power")])})
                                      
OptionFactory = Factory(Option, [PrimitiveParameter("description"), ComplexParameter("effects", EffectFactory.loadAll), ComplexParameter("condition", ConditionFactory.load, optional=True)])

EffectFactory.addFactory("AS_NEXT_PLAYER", Factory(AsNextPlayer, [ComplexParameter("then", EffectFactory.loadAll)]))
EffectFactory.addFactory("AS_PLAYER_WITH_HIGHEST_COST", Factory(AsPlayerWithHighestCost, [PrimitiveParameter("source"), ComplexParameter("then", EffectFactory.loadAll)]))
EffectFactory.addFactory("AS_ONLY_PLAYER_WITH_HIGHEST_COST", Factory(AsOnlyPlayerWithHighestCost, [ComplexParameter("then", EffectFactory.loadAll)]))
EffectFactory.addFactory("AS_PREVIOUS_PLAYER", Factory(AsPreviousPlayer, [ComplexParameter("then", EffectFactory.loadAll)]))
EffectFactory.addFactory("AS_OWNER", Factory(AsOwner, [ComplexParameter("then", EffectFactory.loadAll)]))
EffectFactory.addFactory("ATTACK", Factory(Attack, [ComplexParameter("then", EffectFactory.loadAll)]))
EffectFactory.addFactory("ATTACK_EACH_FOE", Factory(AttackEachFoe, [ComplexParameter("effects", EffectFactory.loadAll)]))
EffectFactory.addFactory("CHOICE", Factory(Choice, [ComplexParameter("choices", OptionFactory.loadAll), PrimitiveParameter("source", optional=True), ComparisonFilterParameter(optional=True)]))
EffectFactory.addFactory("CONDITIONAL", Factory(ConditionalEffect, [ComplexParameter("condition", ConditionFactory.load), 
                                                                    ComplexParameter("effects", EffectFactory.loadAll), 
                                                                    ComplexParameter("otherwise", EffectFactory.load, optional=True)]))
EffectFactory.addFactory("COLLECT_CARDS", Factory(CollectCards, [ComplexParameter("then", EffectFactory.loadAll), PrimitiveParameter("from", optional=True), 
                                                                 PrimitiveParameter("pick", optional=True), PrimitiveParameter("number", optional=True)]))
EffectFactory.addFactory("FILTER", Factory(Filter, [PrimitiveParameter("source"), FilterParameter(), ComplexParameter("then", EffectFactory.loadAll)]))
EffectFactory.addFactory("LOOK_AT_TOP", Factory(LookAtTop, [PrimitiveParameter("source"), ComplexParameter("then", EffectFactory.loadAll)]))
EffectFactory.addFactory("PER_FOE", Factory(PerFoe, [ComplexParameter("effects", EffectFactory.loadAll)]))
EffectFactory.addFactory("PER_MATCH", Factory(PerMatch, [PrimitiveParameter("source"), ComplexParameter("effects", EffectFactory.loadAll), FilterParameter(optional=True)]))
EffectFactory.addFactory("PICK_CARDS", Factory(PickCards, [PrimitiveParameter("sources"), PrimitiveParameter("number"), 
                                                           ComplexParameter("then", EffectFactory.loadAll), ComplexParameter("criteria", CriteriaFactory.loadAll, optional=True)]))
EffectFactory.addFactory("PICK_RANDOM", Factory(PickRandomCard, [PrimitiveParameter("source"), ComplexParameter("then", EffectFactory.load), PrimitiveParameter("number", optional=True)]))
EffectFactory.addFactory("PICK_UP_TO_ALL_CARDS", Factory(PickUpToAllCards, [PrimitiveParameter("sources"), ComplexParameter("then", EffectFactory.loadAll), 
                                                                            ComplexParameter("criteria", CriteriaFactory.loadAll, optional=True)]))
EffectFactory.addFactory("PICK_UP_TO_N_CARDS", Factory(PickUpToNCards, [PrimitiveParameter("sources"), PrimitiveParameter("number"), 
                                                                        ComplexParameter("then", EffectFactory.loadAll), ComplexParameter("criteria", CriteriaFactory.loadAll, optional=True)]))
EffectFactory.addFactory("PLAY_OR_HAVE_PLAYED", Factory(PlayOrHavePlayed, [ComplexParameter("effect", EffectFactory.load), ComplexParameter("criteria", CriteriaFactory.load), 
                                                                           PrimitiveParameter("singleUse", optional=True)]))
EffectFactory.addFactory("PLAY_OR_HAVE_PLAYED_ANOTHER", Factory(PlayOrHavePlayedAnother, [ComplexParameter("effect", EffectFactory.load), ComplexParameter("criteria", CriteriaFactory.load)]))