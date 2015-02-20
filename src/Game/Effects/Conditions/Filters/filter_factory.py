from comparison_filter import ComparisonFilter
from intersection_filter import IntersectionFilter
from zones_filter import ZonesFilter
from unique_filter import UniqueFilter

from Game.Effects.Conditions.Filters.Criteria.criteria_factory import CriteriaFactory
from Game.Factory.zone_type_parameter import ZoneTypeParameter
from Game.Factory.zone_types_parameter import ZoneTypesParameter

from kao_factory.factory import Factory
from kao_factory.typed_factory import TypedFactory
from kao_factory.Parameter.complex_parameter import ComplexParameter
from kao_factory.Parameter.primitive_parameter import PrimitiveParameter

FilterFactory = TypedFactory('type', {"COMPARISON":Factory(ComparisonFilter, [ZoneTypeParameter("zone"), ComplexParameter("criteria", CriteriaFactory.load)]),
                                      "ZONES":Factory(ZonesFilter, [ZoneTypesParameter("zones")]),
                                      "UNIQUE":Factory(UniqueFilter, [PrimitiveParameter("field"), ZoneTypeParameter("zone")])})
FilterFactory.addFactory("INTERSECTION", Factory(IntersectionFilter, [ComplexParameter("filters", FilterFactory.loadAll)]))
FilterFactory.addFactory("UNION", Factory(IntersectionFilter, [ComplexParameter("filters", FilterFactory.loadAll)]))