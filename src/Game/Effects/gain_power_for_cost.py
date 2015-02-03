from Game.Effects.effect_runner import PerformEffect
from Game.Effects.gain_power import GainPower

class GainPowerForCost:
    """ Represents an effect that gains power for the playing player """
    
    def __init__(self, zoneType):
        """ Initialize the Effect with the zoneType to gain power from """
        self.zoneType = zoneType
        
    def perform(self, context):
        """ Perform the Game Effect """
        for card in context.loadZone(self.zoneType):
            coroutine = PerformEffect(GainPower(card.cost), context)
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response)