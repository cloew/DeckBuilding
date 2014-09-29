from comparison_filter import ComparisonFilter
from intersection_filter import IntersectionFilter
from unique_filter import UniqueFilter

from Game.Effects.Conditions.Filters.Criteria.criteria_factory import CriteriaFactory

class FilterFactory:
    """ Factory to build Filters """
    
    def loadFilter(self, filterJSON):
        """ Load the Filter from the given JSON """
        if filterJSON["type"] == "COMPARISON":
            criteria = CriteriaFactory.load(filterJSON["criteria"])
            return ComparisonFilter(filterJSON["sourceType"], criteria)
        elif filterJSON["type"] == "INTERSECTION":
            filters = [self.loadFilter(subFilterJSON) for subFilterJSON in filterJSON["filters"]]
            return IntersectionFilter(filters)
        elif filterJSON["type"] == "UNIQUE":
            return ComparisonFilter(filterJSON["field"], filterJSON["sourceType"])
        else:
            print "Cannot find Filter:", filterJSON["type"]
        return None
        
FilterFactory = FilterFactory()