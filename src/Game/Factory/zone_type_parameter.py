from Game.Zones.zone_types import nameToZoneType
from kao_factory.Parameter.primitive_parameter import PrimitiveParameter

class ZoneTypeParameter(PrimitiveParameter):
    """ Represents a zone type parameter """
    
    def __getvalue__(self, data):
        """ Build the Filter """
        return nameToZoneType[PrimitiveParameter.__getvalue__(self, data)]