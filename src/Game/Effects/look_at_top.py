from Game.Effects.conditional_effect import ConditionalEffect
from Game.Effects.Conditions.has_cards import HasCards
from Game.Events.top_card_event import TopCardEvent
from Game.Sources.source_factory import SourceFactory

class LookAtTop(ConditionalEffect):
    """ Represents an effect to Look at the top Card of a source """
    
    def __init__(self, sourceType, thenEffect):
        """ Initialize the Effect with the source to look at """
        self.sourceType = sourceType
        ConditionalEffect.__init__(self, HasCards(self.sourceType), thenEffect)
        
    def performEffect(self, args):
        """ Perform the Game Effect """
        source = SourceFactory.getSource(self.sourceType, args.game, event=args.event)
        card = source[0]
        event = TopCardEvent(card, source, args.game)
        
        coroutine = ConditionalEffect.performEffect(self, event.args)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)