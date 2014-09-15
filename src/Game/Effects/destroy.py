from Game.Commands.Requests.pick_card_request import PickCardRequest
from Game.Sources.source_factory import SourceFactory, DESTROYED, HAND

class Destroy:
    """ Represents an effect to Destroy Cards """
    
    def __init__(self):
        """ Initialize the Effect """
        self.sourceType = HAND
        
    def perform(self, args):
        """ Perform the Game Effect """
        source = SourceFactory.getSource(self.sourceType, args.game)
        destroyedDeck = SourceFactory.getSource(DESTROYED, args.game)
        card = yield PickCardRequest(source)
        
        source.remove(card)
        destroyedDeck.add(card)