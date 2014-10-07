from and_condition import AndCondition
from matching import Matching
from unique import Unique

from Game.Effects.Conditions.Filters.comparison_filter import ComparisonFilter
from Game.Effects.Conditions.Filters.intersection_filter import IntersectionFilter
from Game.Effects.Conditions.Filters.unique_filter import UniqueFilter

from Game.Sources.source_types import PLAYED

class NthUnique:
    """ Condition to check if a condition is the nth uniqe card played """
    
    def __init__(self, n, criterion):
        """ Initialize the condition with the value of n """
        self.n = n
        self.playedFilter = self.getFilter(criterion)
        self.eventCondition = self.getEventCondition(criterion)
        
    def evaluate(self, context):
        """ Evaluate the condition """
        return self.eventCondition.evaluate(context) and len(self.playedFilter.evaluate(context)) == self.n-1
        
    def getFilter(self, criterion):
        """ Return the filter """
        filters = [UniqueFilter("name", PLAYED)] + [ComparisonFilter(PLAYED, criteria) for criteria in criterion]
        return IntersectionFilter(filters)
        
    def getEventCondition(self, criterion):
        """ Return the event condition """
        conditions = [Unique("name", PLAYED)] + [Matching(PLAYED, criteria) for criteria in criterion]
        return AndCondition(conditions)