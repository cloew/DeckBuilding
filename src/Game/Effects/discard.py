from Game.Sources.source_factory import SourceFactory, DISCARD_PILE, HAND

class Discard:
    """ Represents an effect to Discard Cards """
    
    def __init__(self):
        """ Initialize the Effect """
        self.sourceType = HAND
        
    def perform(self, args):
        """ Perform the Game Effect """
        source = SourceFactory.getSource(self.sourceType, args.game)
        discardPile = SourceFactory.getSource(DISCARD_PILE, args.game)
        
        for card in list(source):
            source.remove(card)
            discardPile.add(card)