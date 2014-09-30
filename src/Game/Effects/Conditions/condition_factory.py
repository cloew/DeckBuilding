from and_condition import AndCondition
from enough_power import EnoughPower
from has_cards import HasCards
from matching import Matching
from not_condition import NotCondition
from nth_played import NthPlayed
from nth_unique import NthUnique
from or_condition import OrCondition
from unique import Unique

from Game.Effects.Conditions.Filters.Criteria.criteria_factory import CriteriaFactory

from Game.Factory.comparison_filter_parameter import ComparisonFilterParameter

from kao_factory.factory import Factory
from kao_factory.typed_factory import TypedFactory
from kao_factory.Parameter.complex_parameter import ComplexParameter
from kao_factory.Parameter.primitive_parameter import PrimitiveParameter

ConditionFactory = TypedFactory('type', {"ENOUGH_POWER":Factory(EnoughPower, [PrimitiveParameter("power")]),
                                         "HAS_CARDS":Factory(HasCards, [PrimitiveParameter("sourceType"), ComparisonFilterParameter(optional=True)]),
                                         "MATCHING":Factory(Matching, [PrimitiveParameter("sourceType"), ComplexParameter("criteria", CriteriaFactory.load), PrimitiveParameter("number", optional=True)]),
                                         "NTH":Factory(NthPlayed, [PrimitiveParameter("n"), ComplexParameter("criteria", CriteriaFactory.load)]),
                                         "NTH_UNIQUE":Factory(NthUnique, [PrimitiveParameter("n"), ComplexParameter("criterion", CriteriaFactory.loadAll, optional=True, default=[])]),
                                         "UNIQUE":Factory(Unique, [PrimitiveParameter("field"), PrimitiveParameter("source")]),
                                         })
ConditionFactory.addFactory("AND", Factory(AndCondition, [ComplexParameter("conditions", ConditionFactory.loadAll)]))
ConditionFactory.addFactory("NOT", Factory(NotCondition, [ComplexParameter("condition", ConditionFactory.load)]))
ConditionFactory.addFactory("OR", Factory(OrCondition, [ComplexParameter("conditions", ConditionFactory.loadAll)]))