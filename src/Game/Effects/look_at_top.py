from Game.Events.top_card_event import TopCardEvent
from Game.Sources.source_factory import SourceFactory

class LookAtTop:
    """ Represents an effect to Look at the top Card of a source """
    
    def __init__(self, sourceType, thenEffect):
        """ Initialize the Effect with the source to look at """
        self.sourceType = sourceType
        self.thenEffect = thenEffect
        
    def perform(self, args):
        """ Perform the Game Effect """
        source = SourceFactory.getSource(self.sourceType, args.game, event=args.event)
        card = source[0]
        event = TopCardEvent(card, source, args.game)
        self.thenEffect.perform(event.args)