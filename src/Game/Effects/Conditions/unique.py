from Game.Effects.Conditions.matching import Matching
from Game.Effects.Conditions.not_condition import NotCondition
from Game.Effects.Conditions.Filters.Criteria.source_criteria import SourceCriteria

from Game.Sources.source_factory import EVENT

class Unique:
    """ Represents a condition where a field must match a value """
    
    def __init__(self, field, sourceType):
        """ Initialize the Matching Condition with the field to use and the values it can match """
        matchingCondition = Matching(EVENT, SourceCriteria(field, sourceType))
        self.condition = NotCondition(matchingCondition)
        
    def evaluate(self, game, event=None):
        """ Evaluate the condition """
        return self.condition.evaluate(game, event=event)