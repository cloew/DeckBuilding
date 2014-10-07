from Game.Effects.Conditions.Filters.comparison_filter import ComparisonFilter
from matching import Matching

from Game.Sources.source_types import EVENT, PLAYED

class NthPlayed:
    """ Condition to check if a condition is the nth card played """
    
    def __init__(self, n, criteria):
        """ Initialize the condition with the value of n """
        self.n = n
        self.playedFilter = ComparisonFilter(PLAYED, criteria)
        self.eventCondition = Matching(EVENT, criteria)
        
    def evaluate(self, context):
        """ Evaluate the condition """
        return self.eventCondition.evaluate(context) and len(self.playedFilter.evaluate(context)) == self.n-1