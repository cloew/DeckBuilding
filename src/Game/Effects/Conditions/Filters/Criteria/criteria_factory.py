from fixed_criteria import FixedCriteria
from source_criteria import SourceCriteria

class CriteriaFactory:
    """ Factory to build Criterion """
    
    def loadCriteria(self, criteriaJSON):
        """ Load the Criteria from the given JSON """
        if criteriaJSON["type"] == "FIXED":
            return FixedCriteria(criteriaJSON["field"], criteriaJSON["value"], criteriaJSON["operation"])
        elif criteriaJSON["type"] == "SOURCE":
            return SourceCriteria(criteriaJSON["field"], criteriaJSON["source"])
        else:
            print "Cannot find Criteria:", criteriaJSON["type"]
        return None
        
CriteriaFactory = CriteriaFactory()