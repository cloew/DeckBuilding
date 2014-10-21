from Game.Effects.conditional_effect import ConditionalEffect
from Game.Effects.Conditions.has_cards import HasCards
from Game.Events.cards_event import CardsEvent

import random

class PickRandomCard(ConditionalEffect):
    """ Represents an effect to Pick a Random Card of a source """
    
    def __init__(self, sourceType, thenEffect, number=None):
        """ Initialize the Effect with the source to look at """
        self.sourceType = sourceType
        
        if number is None:
            number = 1
        self.number = number
        
        ConditionalEffect.__init__(self, HasCards(self.sourceType), [thenEffect])
        
    def performEffects(self, context):
        """ Perform the Game Effect """
        event = self.getRandomCards(context)
        
        coroutine = ConditionalEffect.performEffects(self, event.context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)
            
    def getRandomCards(self, context):
        """ Get Random Cards and return the proper event """
        source = context.loadSource(self.sourceType)
        cards = random.sample(source, self.getNumberOfCards(source))
        return CardsEvent(cards, source, context)
        
    def getNumberOfCards(self, source):
        """ Return the number of cards that can be picked """
        return min(self.number, len(source)) 