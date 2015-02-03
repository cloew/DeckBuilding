from Game.Effects.look_at_top import LookAtTop
from Game.Effects.gain_card import GainCard
from Game.Zones.zone_types import EVENT

class GainTopCard(LookAtTop):
    """ Represents an effect to Look at the top Card of a zone """
    
    def __init__(self, fromZoneType, toZoneType=None):
        """ Initialize the Effect with the zone to look at """
        LookAtTop.__init__(self, fromZoneType, [GainCard(EVENT, toZoneType=toZoneType)])