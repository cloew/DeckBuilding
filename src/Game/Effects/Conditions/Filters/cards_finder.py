
class CardsFinder:
    """ Helper class to find cards from a zone and an optional filter """
    
    def __init__(self, zoneType, filter):
        """ Initialize the Card Finder """
        self.zoneType = zoneType
        self.filter = filter
        
    def find(self, context):
        """ Return the cards """
        zone = context.loadZone(self.zoneType)
        cards = zone
        if self.filter is not None:
            cards = self.filter.evaluate(context)
        
        return zone, cards