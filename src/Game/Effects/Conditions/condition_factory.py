from and_condition import AndCondition
from enough_power import EnoughPower
from filter_results import FilterResults
from has_cards import HasCards
from is_player_character import IsPlayerCharacter
from is_player_turn import IsPlayerTurn
from matching import Matching
from not_condition import NotCondition
from nth_played import NthPlayed
from nth_unique import NthUnique
from or_condition import OrCondition
from unique import Unique

from Game.Effects.Conditions.Filters.Criteria.criteria_factory import CriteriaFactory

from Game.Factory.intersection_filter_parameter import IntersectionFilterParameter
from Game.Factory.filter_parameter import FilterParameter

from kao_factory.factory import Factory
from kao_factory.typed_factory import TypedFactory
from kao_factory.Parameter.complex_parameter import ComplexParameter
from kao_factory.Parameter.primitive_parameter import PrimitiveParameter

ConditionFactory = TypedFactory('type', {"ENOUGH_POWER":Factory(EnoughPower, [PrimitiveParameter("power")]),
                                         "FILTER_RESULTS":Factory(FilterResults, [PrimitiveParameter("source"), FilterParameter(), PrimitiveParameter("number", optional=True)]),
                                         "IS_PLAYER_CHARACTER":Factory(IsPlayerCharacter, []),
                                         "IS_PLAYER_TURN":Factory(IsPlayerTurn, []),
                                         "HAS_CARDS":Factory(HasCards, [PrimitiveParameter("source"), IntersectionFilterParameter(optional=True)]),
                                         "MATCHING":Factory(Matching, [PrimitiveParameter("source"), ComplexParameter("criteria", CriteriaFactory.load, optional=True), PrimitiveParameter("number", optional=True)]),
                                         "NTH":Factory(NthPlayed, [PrimitiveParameter("n"), ComplexParameter("criteria", CriteriaFactory.load)]),
                                         "NTH_UNIQUE":Factory(NthUnique, [PrimitiveParameter("n"), ComplexParameter("criterion", CriteriaFactory.loadAll, optional=True, default=[]), PrimitiveParameter("field", optional=True)]),
                                         "UNIQUE":Factory(Unique, [PrimitiveParameter("field"), PrimitiveParameter("source")]),
                                         })
ConditionFactory.addFactory("AND", Factory(AndCondition, [ComplexParameter("conditions", ConditionFactory.loadAll)]))
ConditionFactory.addFactory("NOT", Factory(NotCondition, [ComplexParameter("condition", ConditionFactory.load)]))
ConditionFactory.addFactory("OR", Factory(OrCondition, [ComplexParameter("conditions", ConditionFactory.loadAll)]))