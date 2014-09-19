from fixed_criteria import FixedCriteria

class CriteriaFactory:
    """ Factory to build Criterion """
    
    def loadCriteria(self, criteriaJSON):
        """ Load the Criteria from the given JSON """
        if criteriaJSON["type"] == "FIXED":
            return FixedCriteria(criteriaJSON["field"], criteriaJSON["value"], criteriaJSON["operation"])
        else:
            print "Cannot find Criteria:", criteriaJSON["type"]
        return None
        
CriteriaFactory = CriteriaFactory()