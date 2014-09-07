from matching import Matching

class ConditionFactory:
    """ Factory to build Conditions """
    
    def loadCondition(self, conditionJSON):
        """ Load the Condition from the given JSON """
        if conditionJSON["type"] == "MATCHING":
            return Matching(conditionJSON["field"], conditionJSON["values"], conditionJSON["sourceType"])
        return None
        
ConditionFactory = ConditionFactory()