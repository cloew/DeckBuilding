from Game.Sources.source_factory import SourceFactory, DISCARD_PILE, HAND

class Discard:
    """ Represents an effect to Discard Cards """
    
    def __init__(self, sourceType):
        """ Initialize the Effect with the Source to Discard from """
        self.sourceType = sourceType
        
    def perform(self, context):
        """ Perform the Game Effect """
        source = SourceFactory.getSourceForEffect(self.sourceType, context)
        discardPile = SourceFactory.getSourceForEffect(DISCARD_PILE, context)
        
        for card in list(source):
            source.remove(card)
            discardPile.add(card)