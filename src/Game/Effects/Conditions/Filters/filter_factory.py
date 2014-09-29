from comparison_filter import ComparisonFilter
from intersection_filter import IntersectionFilter
from unique_filter import UniqueFilter

from Game.Effects.Conditions.Filters.Criteria.criteria_factory import CriteriaFactory

from kao_factory.factory import Factory
from kao_factory.typed_factory import TypedFactory
from kao_factory.Parameter.complex_parameter import ComplexParameter
from kao_factory.Parameter.primitive_parameter import PrimitiveParameter

FilterFactory = TypedFactory('type', {"COMPARISON":Factory(ComparisonFilter, [PrimitiveParameter("sourceType"), ComplexParameter("criteria", CriteriaFactory.load)]),
                                      "UNIQUE":Factory(UniqueFilter, [PrimitiveParameter("field"), PrimitiveParameter("sourceType")])})
FilterFactory.addFactory("INTERSECTION", Factory(IntersectionFilter, [ComplexParameter("filters", FilterFactory.loadAll)]))
 
# class FilterFactory:
    # """ Factory to build Filters """
    
    # def loadFilter(self, filterJSON):
        # """ Load the Filter from the given JSON """
        # if filterJSON["type"] == "COMPARISON":
            # criteria = CriteriaFactory.load(filterJSON["criteria"])
            # return ComparisonFilter(filterJSON["sourceType"], criteria)
        # elif filterJSON["type"] == "INTERSECTION":
            # filters = [self.loadFilter(subFilterJSON) for subFilterJSON in filterJSON["filters"]]
            # return IntersectionFilter(filters)
        # elif filterJSON["type"] == "UNIQUE":
            # return ComparisonFilter(filterJSON["field"], filterJSON["sourceType"])
        # else:
            # print "Cannot find Filter:", filterJSON["type"]
        # return None
        
# FilterFactory = FilterFactory()