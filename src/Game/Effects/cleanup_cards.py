from Game.Events.cards_event import CardsEvent
from Game.Effects.effect_runner import PerformEffects
from Game.Zones.zone_types import PLAYED, EVENT

class CleanupCards:
    """ Effect to allow cleanup effects to modify the parent card """
    
    def __init__(self, cards, zoneType, thenEffects):
        """ Initialize the Cleanup """
        self.cards = cards
        self.zoneType = zoneType
        self.thenEffects = thenEffects
    
    def perform(self, context):
        """ Perform the Game Effect """
        zone = context.loadZone(self.zoneType)
        cards = [card for card in self.cards if card in zone]
        
        if len(cards) > 0:
            event = CardsEvent(cards, zone, context)
            
            coroutine = PerformEffects(self.thenEffects, event.context)
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response)