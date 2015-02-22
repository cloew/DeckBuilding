from Game.Events.cards_event import CardsEvent
from Game.Zones.zone_types import EVENT

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
        
    def findAsEvent(self, context):
        """ Return the cards as an Event Zone """
        zone, cards = self.find(context)
        event = CardsEvent(cards, zone, context)
        return event.context.loadZone(EVENT)