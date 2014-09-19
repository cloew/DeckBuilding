from Game.Effects.Conditions.Filters.comparison_filter import ComparisonFilter
from matching import Matching

from Game.Sources.source_factory import EVENT, PLAYED

class NthPlayed:
    """ Condition to check if a condition is the nth card played """
    
    def __init__(self, n, criteria):
        """ Initialize the condition with the value of n """
        self.n = n
        self.playedFilter = ComparisonFilter(PLAYED, criteria)
        self.eventCondition = Matching(EVENT, criteria)
        
    def evaluate(self, game, event=None):
        """ Evaluate the condition """
        return self.eventCondition.evaluate(game, event=event) and len(self.playedFilter.evaluate(game, event=event)) == self.n-1