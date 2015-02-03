from Game.Effects.conditional_effect import ConditionalEffect
from Game.Effects.Conditions.has_cards import HasCards
from Game.Events.cards_event import CardsEvent

import random

class PickRandomCard(ConditionalEffect):
    """ Represents an effect to Pick a Random Card of a zone """
    
    def __init__(self, zoneType, thenEffect, number=None):
        """ Initialize the Effect with the zone to look at """
        self.zoneType = zoneType
        
        if number is None:
            number = 1
        self.number = number
        
        ConditionalEffect.__init__(self, HasCards(self.zoneType), [thenEffect])
        
    def performEffects(self, context):
        """ Perform the Game Effect """
        event = self.getRandomCards(context)
        
        coroutine = ConditionalEffect.performEffects(self, event.context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)
            
    def getRandomCards(self, context):
        """ Get Random Cards and return the proper event """
        zone = context.loadzone(self.zoneType)
        cards = random.sample(zone, self.getNumberOfCards(zone))
        return CardsEvent(cards, zone, context)
        
    def getNumberOfCards(self, zone):
        """ Return the number of cards that can be picked """
        return min(self.number, len(zone)) 