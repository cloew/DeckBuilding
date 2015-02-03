from Game.Effects.Conditions.filter_results import FilterResults
from Game.Effects.Conditions.Filters.comparison_filter import ComparisonFilter

class Matching(FilterResults):
    """ Represents a condition where a field must match a value """
    
    def __init__(self, zoneType, criteria=None, number=None):
        """ Initialize the Matching Condition with the criteria to use """
        filter = None
        if criteria is not None:
            filter = ComparisonFilter(zoneType, criteria)
        FilterResults.__init__(self, zoneType, filter=filter, number=number)