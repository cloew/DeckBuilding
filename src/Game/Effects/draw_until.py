from Game.Effects.draw import Draw
from Game.Effects.effect_runner import PerformEffects
from Game.Effects.look_at_top import LookAtTop
from Game.Effects.reveal import Reveal
from Game.Sources.source_types import DECK, EVENT

class DrawUntil:
    """ Represents an effect to Draw Cards until a certain cost has been drawn """
    
    def __init__(self, cost):
        """ Initialize the Effect with the cost of cards to draw """
        self.cost = cost
        self.lookAtTop = LookAtTop(EVENT, [Reveal(EVENT)])
        
    def perform(self, context):
        """ Perform the Game Effect """
        totalCost = 0
        while totalCost < self.cost:
            source = context.loadSource(DECK)
            if source.availableLength() > 0:
                card = source[0]
                totalCost += card.cost
            
                coroutine = PerformEffects([self.lookAtTop, Draw(1)], context)
                response = yield coroutine.next()
                while True:
                    response = yield coroutine.send(response)