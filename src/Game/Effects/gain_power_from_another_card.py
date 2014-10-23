from Game.Effects.effect_runner import PerformEffect
from Game.Effects.gain_power import GainPower
from Game.Effects.pick_cards import PickCards

class GainPowerFromAnotherCard:
    """ Represents an effect that gains power equal to the amount gained from another card """
    
    def __init__(self, sourceType):
        """ Initialize the Effect with the sourceType to gain power from """
        self.sourceType = sourceType
        
    def perform(self, context):
        """ Perform the Game Effect """
        for card in context.loadSource(self.sourceType):
            coroutine = PerformEffect(GainPower(context.owner.getPowerForCard(card)), context)
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response)