from Game.Commands.Requests.pick_card_request import PickCardRequest
from Game.Sources.source_factory import SourceFactory

class MoveCard:
    """ Represents an effect to Move a Card """
    
    def __init__(self, fromSourceType, toSourceType):
        """ Initialize the Effect """
        self.fromSourceType = fromSourceType
        self.toSourceType = toSourceType
        
    def perform(self, args):
        """ Perform the Game Effect """
        fromSource = SourceFactory.getSourceForEffect(self.fromSourceType, args)
        toSource = SourceFactory.getSourceForEffect(self.toSourceType, args)
        
        for card in list(fromSource):
            fromSource.remove(card)
            toSource.add(card)