from Game.Sources.source_factory import SourceFactory, DISCARD_PILE

class GainCard:
    """ Represents an effect to Gain a card """
    
    def __init__(self, fromSourceType, toSourceType=DISCARD_PILE):
        """ Initialize the Effect with the card to remove from play before discarding """
        self.fromSourceType = fromSourceType
        self.toSourceType = toSourceType
        
    def perform(self, args):
        """ Perform the Game Effect """
        fromSource = SourceFactory.getSource(self.fromSourceType, args.game, event=args.event)
        toSource = SourceFactory.getSource(self.toSourceType, args.game, event=args.event)
        
        for card in fromSource:
            args.owner.gainCard(card, fromSource, toSource=toSource)