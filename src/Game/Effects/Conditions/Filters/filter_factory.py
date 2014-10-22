from comparison_filter import ComparisonFilter
from intersection_filter import IntersectionFilter
from unique_filter import UniqueFilter

from Game.Effects.Conditions.Filters.Criteria.criteria_factory import CriteriaFactory

from kao_factory.factory import Factory
from kao_factory.typed_factory import TypedFactory
from kao_factory.Parameter.complex_parameter import ComplexParameter
from kao_factory.Parameter.primitive_parameter import PrimitiveParameter

FilterFactory = TypedFactory('type', {"COMPARISON":Factory(ComparisonFilter, [PrimitiveParameter("source"), ComplexParameter("criteria", CriteriaFactory.load)]),
                                      "UNIQUE":Factory(UniqueFilter, [PrimitiveParameter("field"), PrimitiveParameter("source")])})
FilterFactory.addFactory("INTERSECTION", Factory(IntersectionFilter, [ComplexParameter("filters", FilterFactory.loadAll)]))