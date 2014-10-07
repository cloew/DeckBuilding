from Game.Effects.move_card import MoveCard
from Game.Sources.source_types import DISCARD_PILE

class Discard(MoveCard):
    """ Represents an effect to Discard Cards """
    
    def __init__(self, sourceType):
        """ Initialize the Effect with the Source to Discard from """
        MoveCard.__init__(self, sourceType, DISCARD_PILE)