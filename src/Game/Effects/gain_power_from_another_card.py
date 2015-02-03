from Game.Effects.effect_runner import PerformEffect
from Game.Effects.gain_power import GainPower
from Game.Effects.pick_cards import PickCards

class GainPowerFromAnotherCard:
    """ Represents an effect that gains power equal to the amount gained from another card """
    
    def __init__(self, zoneType):
        """ Initialize the Effect with the zoneType to gain power from """
        self.zoneType = zoneType
        
    def perform(self, context):
        """ Perform the Game Effect """
        for card in context.loadZone(self.zoneType):
            try:
                coroutine = PerformEffect(GainPower(context.owner.getPowerForCard(card)), context)
                response = yield coroutine.next()
                while True:
                    response = yield coroutine.send(response)
            except StopIteration:
                pass