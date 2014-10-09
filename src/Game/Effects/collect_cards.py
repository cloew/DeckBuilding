from Game.Effects.effect_runner import PerformEffects
from Game.Events.cards_event import CardsEvent
from Game.Sources.source_types import DECK

class CollectCards:
    """ Represents an effect to Collect Cards from the top of your opponents decks """
    
    def __init__(self, thenEffects, sourceType=None, number=None):
        """ Initialize the Effect with the effects to call with the collected cards """
        self.thenEffects = thenEffects
        if sourceType is None:
            sourceType = DECK
        self.sourceType = sourceType
        if number is None:
            number = 1
        self.number = number
        
    def perform(self, context):
        """ Perform the Game Effect """
        collectedCards = [card for foe in context.foes for card in self.getTopCards(context.getPlayerContext(foe).loadSource(self.sourceType), self.number)]
                
        event = CardsEvent(collectedCards, None, context)
        coroutine = PerformEffects(self.thenEffects, event.context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)
            
    def getTopCards(self, source, number):
        """ Get the Top Cards """
        return source[:number]