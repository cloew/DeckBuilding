from Game.Commands.Requests.pick_card_request import PickCardRequest
from Game.Sources.source_factory import SourceFactory

class MoveCard:
    """ Represents an effect to Move a Card """
    
    def __init__(self, fromSourceType, toSourceType, filter=None):
        """ Initialize the Effect """
        self.fromSourceType = fromSourceType
        self.toSourceType = toSourceType
        self.filter = filter
        
    def perform(self, args):
        """ Perform the Game Effect """
        fromSource = SourceFactory.getSourceForEffect(self.fromSourceType, args)
        toSource = SourceFactory.getSourceForEffect(self.toSourceType, args)
        
        cards = fromSource
        if self.filter is not None:
            cards = self.filter.evaluate(args.game)
        
        card = None
        if len(cards) == 1:
            card = cards[0]
        else:
            card = yield PickCardRequest(cards)
        
        fromSource.remove(card)
        toSource.add(card)