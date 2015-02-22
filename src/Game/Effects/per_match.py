from effect_runner import PerformEffects
from Game.Effects.Conditions.Filters.cards_finder import CardsFinder
from Game.Events.cards_event import CardsEvent

class PerMatch:
    """ Represents an effect that applies for each matching card """
    
    def __init__(self, zoneType, effects, filter=None):
        """ Initialize the Effect with the condition to evaluate and effect to perform """
        self.effects = effects
        self.cardsFinder = CardsFinder(zoneType, filter)
        
    def perform(self, context):
        """ Perform the Game Effect """
        zone, cards = self.cardsFinder.find(context)
        for card in cards:
            event = CardsEvent([card], zone, context)
            coroutine = PerformEffects(self.effects, event.context)
            try:
                response = yield coroutine.next()
                while True:
                    response = yield coroutine.send(response)
            except StopIteration:
                pass