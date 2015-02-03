from Game.Effects.Conditions.Filters.Operations.operations import operations

class ComparisonFilter:
    """ Represents a filter that returns all the cards from a zone that pass some comparison """
    
    def __init__(self, zoneType, criteria):
        """ Initialize the filter """
        self.zoneType = zoneType
        self.criteria = criteria
        
    def evaluate(self, context):
        """ Evaluate the condition """
        zone = context.loadZone(self.zoneType)
        return [card for card in zone if self.criteria.compare(card, context)]