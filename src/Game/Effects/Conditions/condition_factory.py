from and_condition import AndCondition
from enough_power import EnoughPower
from has_cards import HasCards
from matching import Matching
from not_condition import NotCondition
from nth_played import NthPlayed
from nth_unique import NthUnique
from or_condition import OrCondition
from unique import Unique

from Game.Effects.Conditions.Filters.filter_factory import FilterFactory
from Game.Effects.Conditions.Filters.Criteria.criteria_factory import CriteriaFactory

class ConditionFactory:
    """ Factory to build Conditions """
    
    def loadCondition(self, conditionJSON):
        """ Load the Condition from the given JSON """
        if conditionJSON["type"] == "AND":
            return AndCondition([self.loadCondition(subConditionJSON) for subConditionJSON in conditionJSON["conditions"]])
        elif conditionJSON["type"] == "ENOUGH_POWER":
            return EnoughPower(conditionJSON["power"])
        elif conditionJSON["type"] == "HAS_CARDS":
            filter = None
            if "criteria" in conditionJSON:
                filterJson = {"criteria":conditionJSON["criteria"]}
                filterJson["sourceType"] = conditionJSON["sourceType"]
                filterJson["type"] = "COMPARISON"
                filter = FilterFactory.load(filterJson)
                
            return HasCards(conditionJSON["sourceType"], filter=filter)
        elif conditionJSON["type"] == "MATCHING":
            number = None
            if "number" in conditionJSON:
                number = conditionJSON["number"]
            criteria = CriteriaFactory.load(conditionJSON["criteria"])
            return Matching(conditionJSON["sourceType"], criteria, number=number)
        elif conditionJSON["type"] == "NOT":
            return NotCondition(self.loadCondition(conditionJSON["condition"]))
        elif conditionJSON["type"] == "NTH":
            criteria = CriteriaFactory.load(conditionJSON["criteria"])
            return NthPlayed(conditionJSON["n"], criteria)
        elif conditionJSON["type"] == "NTH_UNIQUE":
            criterion = []
            if "criterion" in conditionJSON:
                criterion = [CriteriaFactory.load(criteriaJSON) for criteriaJSON in conditionJSON["criterion"]]
            return NthUnique(conditionJSON["n"], criterion)
        if conditionJSON["type"] == "OR":
            return OrCondition([self.loadCondition(subConditionJSON) for subConditionJSON in conditionJSON["conditions"]])
        elif conditionJSON["type"] == "UNIQUE":
            return Unique(conditionJSON["field"], conditionJSON["source"])
        else:
            print "Cannot find Condition:", conditionJSON["type"]
        return None
        
ConditionFactory = ConditionFactory()