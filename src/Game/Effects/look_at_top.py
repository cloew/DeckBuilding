from Game.Effects.conditional_effect import ConditionalEffect
from Game.Effects.Conditions.has_cards import HasCards
from Game.Events.cards_event import CardsEvent

class LookAtTop(ConditionalEffect):
    """ Represents an effect to Look at the top Card of a source """
    
    def __init__(self, sourceType, thenEffects, number=None):
        """ Initialize the Effect with the source to look at """
        self.sourceType = sourceType
        if number is None:
            number = 1
        self.number = number
        ConditionalEffect.__init__(self, HasCards(self.sourceType), thenEffects)
        
    def performEffects(self, context):
        """ Perform the Game Effect """
        source = context.loadSource(self.sourceType)
        cards = source[:self.number]
        event = CardsEvent(cards, source, context)
        
        coroutine = ConditionalEffect.performEffects(self, event.context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)