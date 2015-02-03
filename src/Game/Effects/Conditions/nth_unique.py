from and_condition import AndCondition
from matching import Matching
from unique import Unique

from Game.Effects.Conditions.Filters.comparison_filter import ComparisonFilter
from Game.Effects.Conditions.Filters.intersection_filter import IntersectionFilter
from Game.Effects.Conditions.Filters.unique_filter import UniqueFilter

from Game.Zones.zone_types import PLAYED, EVENT

class NthUnique:
    """ Condition to check if a condition is the nth uniqe card played """
    
    def __init__(self, n, criterion=[], field=None):
        """ Initialize the condition with the value of n """
        self.n = n
        if field is None:
            field = "name"
        self.field = field
        self.playedFilter = self.getFilters(criterion)
        self.eventCondition = self.getEventCondition(criterion)
        
    def evaluate(self, context):
        """ Evaluate the condition """
        return self.eventCondition.evaluate(context) and len(self.playedFilter.evaluate(context)) == self.n-1
        
    def getFilters(self, criterion):
        """ Return the filter """
        filters = [UniqueFilter(self.field, PLAYED)] + [ComparisonFilter(PLAYED, criteria) for criteria in criterion]
        return IntersectionFilter(filters)
        
    def getEventCondition(self, criterion):
        """ Return the event condition """
        conditions = [Unique(self.field, PLAYED)] + [Matching(EVENT, criteria) for criteria in criterion]
        return AndCondition(conditions)