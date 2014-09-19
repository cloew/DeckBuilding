from comparison_filter import ComparisonFilter

class FilterFactory:
    """ Factory to build Conditions """
    
    def loadCondition(self, filterJSON):
        """ Load the Condition from the given JSON """
        if filterJSON["type"] == "COMPARISON":
            return ComparisonFilter(filterJson["field"], filterJson["values"], filterJSON["sourceType"], filterJson["operation"])
        else:
            print "Cannot find Filter:", filterJSON["type"]
        return None
        
FilterFactory = FilterFactory()