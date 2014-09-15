from Game.Effects.move_card import MoveCard
from Game.Sources.source_factory import DESTROYED, HAND

class Destroy(MoveCard):
    """ Represents an effect to Destroy Cards """
    
    def __init__(self):
        """ Initialize the Effect """
        MoveCard.__init__(self, HAND, DESTROYED)