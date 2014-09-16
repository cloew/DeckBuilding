from Game.Effects.move_card import MoveCard
from Game.Sources.source_factory import DESTROYED

class Destroy(MoveCard):
    """ Represents an effect to Destroy Cards """
    
    def __init__(self, sourceType):
        """ Initialize the Effect """
        MoveCard.__init__(self, sourceType, DESTROYED)