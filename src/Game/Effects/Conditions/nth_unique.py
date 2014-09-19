from Game.Effects.Conditions.Filters.unique_filter import UniqueFilter
from unique import Unique

from Game.Sources.source_factory import PLAYED

class NthUnique:
    """ Condition to check if a condition is the nth uniqe card played """
    
    def __init__(self, n):
        """ Initialize the condition with the value of n """
        self.n = n
        self.playedFilter = UniqueFilter("name", PLAYED)
        self.eventCondition = Unique("name", PLAYED)
        
    def evaluate(self, game, event=None):
        """ Evaluate the condition """
        return self.eventCondition.evaluate(game, event=event) and len(self.playedFilter.evaluate(game, event=event)) == self.n-1