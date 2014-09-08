from matching import Matching
from not_condition import NotCondition

class ConditionFactory:
    """ Factory to build Conditions """
    
    def loadCondition(self, conditionJSON):
        """ Load the Condition from the given JSON """
        if conditionJSON["type"] == "MATCHING":
            return Matching(conditionJSON["field"], conditionJSON["values"], conditionJSON["sourceType"])
        if conditionJSON["type"] == "NOT":
            return NotCondition(self.loadCondition(conditionJSON["condition"]))
        return None
        
ConditionFactory = ConditionFactory()