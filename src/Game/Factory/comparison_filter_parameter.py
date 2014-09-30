from Game.Effects.Conditions.Filters.filter_factory import FilterFactory
from kao_factory.Parameter.parameter import Parameter

class ComparisonFilterParameter(Parameter):
    """ Parameter that should become a Comparison Filter """
    
    def __init__(self, optional=False, default=None):
        """ Initialize the Comparison Filter Parameter """
        self.field = "criteria"
    
    def __getvalue__(self, data):
        """ Build the Filter """
        filterJson = {"criteria":data["criteria"]}
        filterJson["source"] = data["source"]
        filterJson["type"] = "COMPARISON"
        return FilterFactory.load(filterJson)