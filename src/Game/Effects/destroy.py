from Game.Effects.move_card import MoveCard
from Game.Zones.zone_types import DESTROYED

class Destroy(MoveCard):
    """ Represents an effect to Destroy Cards """
    
    def __init__(self, zoneType):
        """ Initialize the Effect """
        MoveCard.__init__(self, zoneType, DESTROYED)