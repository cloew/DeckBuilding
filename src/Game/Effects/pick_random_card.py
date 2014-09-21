from Game.Effects.conditional_effect import ConditionalEffect
from Game.Effects.Conditions.has_cards import HasCards
from Game.Events.top_card_event import TopCardEvent
from Game.Sources.source_factory import SourceFactory

import random

class PickRandomCard(ConditionalEffect):
    """ Represents an effect to Pick a Random Card of a source """
    
    def __init__(self, sourceType, thenEffect):
        """ Initialize the Effect with the source to look at """
        self.sourceType = sourceType
        ConditionalEffect.__init__(self, HasCards(self.sourceType), thenEffect)
        
    def performEffect(self, args):
        """ Perform the Game Effect """
        source = SourceFactory.getSourceForEffect(self.sourceType, args)
        card = random.choice(source)
        event = TopCardEvent(card, source, args.game)
        
        coroutine = ConditionalEffect.performEffect(self, event.args)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)