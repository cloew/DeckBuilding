from Game.Effects.Conditions.Filters.Operations.operations import operations

class ZonesFilter:
    """ Represents a filter that returns all the cards from a zone """
    
    def __init__(self, zoneTypes):
        """ Initialize the filter """
        self.zoneTypes = zoneTypes
        
    def evaluate(self, context):
        """ Evaluate the condition """
        return [card for zoneType in self.zoneTypes for card in context.loadZone(zoneType)]