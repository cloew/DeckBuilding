from Game.Effects.conditional_effect import ConditionalEffect
from Game.Effects.Conditions.has_cards import HasCards
from Game.Events.cards_event import CardsEvent

import random

class PickRandomCard(ConditionalEffect):
    """ Represents an effect to Pick a Random Card of a source """
    
    def __init__(self, sourceType, thenEffect):
        """ Initialize the Effect with the source to look at """
        self.sourceType = sourceType
        ConditionalEffect.__init__(self, HasCards(self.sourceType), [thenEffect])
        
    def performEffect(self, context):
        """ Perform the Game Effect """
        source = context.loadSource(self.sourceType)
        card = random.choice(source)
        event = CardsEvent([card], source, context)
        
        coroutine = ConditionalEffect.performEffects(self, event.context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)