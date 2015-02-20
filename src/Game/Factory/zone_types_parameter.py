from Game.Zones.zone_types import nameToZoneType
from kao_factory.Parameter.primitive_parameter import PrimitiveParameter

class ZoneTypesParameter(PrimitiveParameter):
    """ Represents a zone types parameter """
    
    def __getvalue__(self, data):
        """ Build the Filter """
        return [nameToZoneType[zoneType] for zoneType in PrimitiveParameter.__getvalue__(self, data)]