from Game.Effects.effect_runner import PerformEffect
from Game.Effects.gain_power import GainPower

class GainPowerForCost:
    """ Represents an effect that gains power for the playing player """
    
    def __init__(self, sourceType):
        """ Initialize the Effect with the sourceType to gain power from """
        self.sourceType = sourceType
        
    def perform(self, context):
        """ Perform the Game Effect """
        for card in context.loadSource(self.sourceType):
            coroutine = PerformEffect(GainPower(card.cost), context)
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response)