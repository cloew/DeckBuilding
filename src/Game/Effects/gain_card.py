from Game.Sources.source_factory import SourceFactory, DISCARD_PILE

class GainCard:
    """ Represents an effect to Gain a card """
    
    def __init__(self, fromSourceType, toSourceType=DISCARD_PILE):
        """ Initialize the Effect with the card to remove from play before discarding """
        self.fromSourceType = fromSourceType
        self.toSourceType = toSourceType
        
    def perform(self, args):
        """ Perform the Game Effect """
        fromSource = SourceFactory.getSourceForEffect(self.fromSourceType, args)
        toSource = SourceFactory.getSourceForEffect(self.toSourceType, args)
        
        for card in fromSource:
            coroutine = args.owner.gainCard(card, fromSource, toSource=toSource)
            try:
                response = yield coroutine.next()
                while True:
                    response = yield coroutine.send(response)
            except StopIteration:
                pass