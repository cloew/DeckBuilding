from Game.Sources.source_factory import SourceFactory

class PutOnBottom:
    """ Represents an effect to Put a Card on the Bottom """
    
    def __init__(self, fromSourceType, toSourceType, card=None):
        """ Initialize the Effect """
        self.card = card
        self.fromSourceType = fromSourceType
        self.toSourceType = toSourceType
        
    def perform(self, args):
        """ Perform the Game Effect """
        fromSource = SourceFactory.getSourceForEffect(self.fromSourceType, args)
        toSource = SourceFactory.getSourceForEffect(self.toSourceType, args)
        
        cards = [self.card]
        if self.card is None:
            cards = list(fromSource)
            
        for card in cards:
            fromSource.remove(card)
            toSource.putOnBottom(card)