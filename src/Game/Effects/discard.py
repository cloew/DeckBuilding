from Game.Effects.move_card import MoveCard
from Game.Zones.zone_types import DISCARD_PILE

class Discard(MoveCard):
    """ Represents an effect to Discard Cards """
    
    def __init__(self, zoneType):
        """ Initialize the Effect with the Zone to Discard from """
        MoveCard.__init__(self, zoneType, DISCARD_PILE)