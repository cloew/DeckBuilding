from Game.Effects.Conditions.Filters.Operations.operations import operations

class ZoneCriteria:
    """ Represents a Criteria based on values from a zone """
    
    def __init__(self, field, zoneType):
        """ Initialize the Fixed Criteria """
        self.field = field
        self.zoneType = zoneType
        self.operation = operations["IN"]
        
    def compare(self, card, context):
        """ Compare the card with the Matching Condition """
        zone = context.loadZone(self.zoneType)
        value = getattr(card, self.field)
        return self.operation(value, [getattr(zoneCard, self.field) for zoneCard in zone])