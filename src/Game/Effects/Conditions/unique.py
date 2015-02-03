from Game.Effects.Conditions.matching import Matching
from Game.Effects.Conditions.not_condition import NotCondition
from Game.Effects.Conditions.Filters.Criteria.zone_criteria import ZoneCriteria

from Game.Zones.zone_types import EVENT

class Unique:
    """ Represents a condition where a field must match a value """
    
    def __init__(self, field, zoneType):
        """ Initialize the Matching Condition with the field to use and the values it can match """
        matchingCondition = Matching(EVENT, ZoneCriteria(field, zoneType))
        self.condition = NotCondition(matchingCondition)
        
    def evaluate(self, context):
        """ Evaluate the condition """
        return self.condition.evaluate(context)