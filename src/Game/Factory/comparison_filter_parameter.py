from Game.Effects.Conditions.Filters.filter_factory import FilterFactory
from Game.Effects.Conditions.Filters.intersection_filter import IntersectionFilter
from kao_factory.Parameter.parameter import Parameter

class ComparisonFilterParameter(Parameter):
    """ Parameter that should become a Comparison Filter """
    
    def __init__(self, optional=False, default=None):
        """ Initialize the Comparison Filter Parameter """
        self.field = "criteria"
        Parameter.__init__(self, optional=optional, default=default)
    
    def __getvalue__(self, data):
        """ Build the Filter """
        if "criterion" not in data:
            criterion = [data["criteria"]]
            
        filters = []
        for criteria in criterion:
            filterJson = {"criteria":data["criteria"]}
            filterJson["source"] = data["source"]
            filterJson["type"] = "COMPARISON"
            filters.append(FilterFactory.load(filterJson))
            
        if len(filters) == 1:
            return filters[0]
        else:
            return IntersectionFilter(filters)