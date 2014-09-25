from Game.Sources.source_factory import SourceFactory

class PutOnBottom:
    """ Represents an effect to Put a Card on the Bottom """
    
    def __init__(self, card, fromSourceType, toSourceType):
        """ Initialize the Effect """
        self.card = card
        self.fromSourceType = fromSourceType
        self.toSourceType = toSourceType
        
    def perform(self, args):
        """ Perform the Game Effect """
        fromSource = SourceFactory.getSourceForEffect(self.fromSourceType, args)
        toSource = SourceFactory.getSourceForEffect(self.toSourceType, args)
        
        fromSource.remove(self.card)
        toSource.putOnBottom(self.card)