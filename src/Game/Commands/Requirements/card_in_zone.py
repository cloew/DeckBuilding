from Game.Zones.zone_factory import ZoneFactory

class CardInZone:
    """ Represents a command requirement that can only be run if the index exists in the zone """
    
    def __init__(self, card, zoneType):
        """ Initialize the requirement with the index and zone type to check """
        self.card = card
        self.zoneType = zoneType
        self.zone = None
    
    def passed(self, player, game):
        """ Return if the requirement passes """
        zone = self.getZone(player, game)
        return self.card in zone
        
    def getZone(self, player, game):
        """ Return the zone to check """
        return ZoneFactory.getZone(self.zoneType, game, player=player)