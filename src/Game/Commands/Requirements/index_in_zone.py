from index_in_list import IndexInList
from Game.Zones.zone_factory import ZoneFactory

class IndexInZone:
    """ Represents a command requirement that can only be run if the index exists in the zone """
    
    def __init__(self, index, zoneType):
        """ Initialize the requirement with the index and zone type to check """
        self.index = index
        self.zoneType = zoneType
        
        self.card = None
        self.zone = None
    
    def passed(self, player, game):
        """ Return if the requirement passes """
        self.zone = self.getZone(player, game)
        indexInListRequirement = IndexInList(self.index, self.zone)
        
        passed = indexInListRequirement.passed(player, game)
        self.card = indexInListRequirement.chosen
        
        return passed
        
    def getZone(self, player, game):
        """ Return the zone to check """
        return ZoneFactory.getZone(self.zoneType, game, player=player)