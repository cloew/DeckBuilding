from Game.Effects.Conditions.Filters.filter_factory import FilterFactory
from Game.Effects.Conditions.Filters.intersection_filter import IntersectionFilter
from kao_factory.Parameter.parameter import Parameter

class IntersectionFilterParameter(Parameter):
    """ Parameter that should become an Intersection Filter """
    
    def __init__(self, optional=False, default=None):
        """ Initialize the Intersection Filter Parameter """
        self.field = "criterion"
        Parameter.__init__(self, optional=optional, default=default)
    
    def __getvalue__(self, data):
        """ Build the Filter """
        criterion = data["criterion"]
            
        filters = []
        for criteria in criterion:
            filterJson = {"criteria":criteria}
            filterJson["source"] = data["source"]
            filterJson["type"] = "COMPARISON"
            filters.append(FilterFactory.load(filterJson))
            
        if len(filters) == 1:
            return filters[0]
        else:
            return IntersectionFilter(filters)