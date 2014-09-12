from Game.Sources.source_factory import SourceFactory, HAND, MAIN_DECK

class GainCard:
    """ Represents an effect to Gain a card """
    
    def __init__(self):
        """ Initialize the Effect with the card to remove from play before discarding """
        self.fromSourceType = MAIN_DECK
        self.toSourceType = HAND
        
    def perform(self, args):
        """ Perform the Game Effect """
        fromSource = SourceFactory.getSource(MAIN_DECK, args.game)
        toSource = SourceFactory.getSource(HAND, args.game)
        
        args.owner.gainCard(fromSource[0], fromSource, toSource=toSource)