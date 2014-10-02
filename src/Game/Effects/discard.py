from Game.Sources.source_factory import DISCARD_PILE

class Discard:
    """ Represents an effect to Discard Cards """
    
    def __init__(self, sourceType):
        """ Initialize the Effect with the Source to Discard from """
        self.sourceType = sourceType
        
    def perform(self, context):
        """ Perform the Game Effect """
        source = context.loadSource(self.sourceType)
        discardPile = context.loadSource(DISCARD_PILE)
        
        for card in list(source):
            source.remove(card)
            discardPile.add(card)