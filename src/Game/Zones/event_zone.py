from zone import Zone

class EventZone(Zone):
    """ Represents a potential zone """
    
    def __init__(self, event, player):
        """ Initialize the zone """
        zoneType = None
        self.event = event
        if hasattr(event, "fromZone") and event.fromZone is not None:
            zoneType = event.fromZone.zoneType
        elif hasattr(event, "zones") and event.zones is not None and len(event.zones) > 0:
            zoneType = event.zones[0].zoneType
        Zone.__init__(self, event, player, zoneType=zoneType)