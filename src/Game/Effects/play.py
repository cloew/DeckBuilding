from Game.Effects.add_to_zone import AddToZone
from Game.Effects.ongoing import Ongoing
from Game.Effects.remove_played_card import RemovePlayedCard

class Play:
    """ Represents an effect to Play Cards """
    EFFECT_TYPES_TO_IGNORE = [Ongoing]
    
    def __init__(self, zoneType, returnTo=None):
        """ Initialize the Effect with the zone to play from """
        self.zoneType = zoneType
        self.returnTo = returnTo
        
    def perform(self, context):
        """ Perform the Game Effect """
        zone = context.loadZone(self.zoneType)
        for card in zone:
            if self.returnTo:
                zone.remove(card)
            context.owner.cleanupEffects.append(RemovePlayedCard(card))
                
            coroutine = context.owner.playCard(card, effectTypesToIgnore=self.EFFECT_TYPES_TO_IGNORE)
            try:
                response = yield coroutine.next()
                while True:
                    response = yield coroutine.send(response)
            except StopIteration:
                pass
                
            if self.returnTo:
                context.owner.cleanupEffects.append(AddToZone(card, context.loadZone(self.returnTo)))