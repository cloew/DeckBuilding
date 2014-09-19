from and_condition import AndCondition
from enough_power import EnoughPower
from has_cards import HasCards
from matching import Matching
from not_condition import NotCondition
from nth_played import NthPlayed

from Game.Effects.Conditions.Filters.filter_factory import FilterFactory

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
            if "filter" in conditionJSON:
                filterJson = dict(conditionJSON["filter"])
                filterJson["sourceType"] = conditionJSON["sourceType"]
                fitlerJson["type"] = "COMPARISON"
                filter = FilterFactory.loadFilter(filterJson)
                
            return HasCards(conditionJSON["sourceType"], filter=filter)
        elif conditionJSON["type"] == "MATCHING":
            return Matching(conditionJSON["field"], conditionJSON["values"], conditionJSON["sourceType"])
        elif conditionJSON["type"] == "NOT":
            return NotCondition(self.loadCondition(conditionJSON["condition"]))
        elif conditionJSON["type"] == "NTH":
            filterJson = conditionJSON["filter"]
            return NthPlayed(conditionJSON["n"], filterJson["field"], filterJson["values"], filterJson["operation"])
        else:
            print "Cannot find Condition:", conditionJSON["type"]
        return None
        
ConditionFactory = ConditionFactory()