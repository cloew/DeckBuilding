from Game.Effects.conditional_effect import ConditionalEffect
from Game.Effects.Conditions.has_cards import HasCards
from Game.Events.cards_event import CardsEvent

class LookAtTop(ConditionalEffect):
    """ Represents an effect to Look at the top Card of a zone """
    
    def __init__(self, zoneType, thenEffects, number=None):
        """ Initialize the Effect with the zone to look at """
        self.zoneType = zoneType
        if number is None:
            number = 1
        self.number = number
        ConditionalEffect.__init__(self, HasCards(self.zoneType), thenEffects)
        
    def performEffects(self, context):
        """ Perform the Game Effect """
        zone = context.loadZone(self.zoneType)
        cards = zone[:self.number]
        event = CardsEvent(cards, zone, context)
        
        coroutine = ConditionalEffect.performEffects(self, event.context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)