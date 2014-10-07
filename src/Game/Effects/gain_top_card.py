from Game.Effects.look_at_top import LookAtTop
from Game.Effects.gain_card import GainCard
from Game.Sources.source_factory import SourceFactory, EVENT

class GainTopCard(LookAtTop):
    """ Represents an effect to Look at the top Card of a source """
    
    def __init__(self, fromSourceType, toSourceType=None):
        """ Initialize the Effect with the source to look at """
        LookAtTop.__init__(self, fromSourceType, [GainCard(EVENT, toSourceType=toSourceType)])