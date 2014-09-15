from and_condition import AndCondition
from has_cards import HasCards
from matching import Matching
from not_condition import NotCondition

from filter import Filter

class ConditionFactory:
    """ Factory to build Conditions """
    
    def loadCondition(self, conditionJSON):
        """ Load the Condition from the given JSON """
        if conditionJSON["type"] == "AND":
            return AndCondition([self.loadCondition(subConditionJSON) for subConditionJSON in conditionJSON["conditions"]])
        elif conditionJSON["type"] == "HAS_CARDS":
            filter = None
            if "filter" in conditionJSON:
                filterJson = conditionJSON["filter"]
                filter = Filter(filterJson["field"], filterJson["values"], conditionJSON["sourceType"])
                
            return HasCards(conditionJSON["sourceType"], filter=filter)
        elif conditionJSON["type"] == "MATCHING":
            return Matching(conditionJSON["field"], conditionJSON["values"], conditionJSON["sourceType"])
        elif conditionJSON["type"] == "NOT":
            return NotCondition(self.loadCondition(conditionJSON["condition"]))
        return None
        
ConditionFactory = ConditionFactory()