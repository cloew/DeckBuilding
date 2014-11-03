from Game.Effects.Conditions.Filters.filter_factory import FilterFactory
from kao_factory.Parameter.parameter import Parameter

class FilterParameter(Parameter):
    """ Parameter that should become a Comparison Filter """
    
    def __init__(self, optional=False, default=None):
        """ Initialize the Comparison Filter Parameter """
        Parameter.__init__(self, "filter", optional=optional, default=default)
    
    def __getvalue__(self, data):
        """ Build the Filter """
        filterJson = data["filter"]
        if "source" not in filterJson and "source" in data:
            filterJson["source"] = data["source"]
        return FilterFactory.load(filterJson)