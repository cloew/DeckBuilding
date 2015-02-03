from Game.Zones.zone_types import DISCARD_PILE

class GainCard:
    """ Represents an effect to Gain a card """
    
    def __init__(self, fromZoneType, toZoneType=None):
        """ Initialize the Effect with the card to remove from play before discarding """
        self.fromZoneType = fromZoneType
        if toZoneType is None:
            toZoneType = DISCARD_PILE
        self.toZoneType = toZoneType
        
    def perform(self, context):
        """ Perform the Game Effect """
        fromZone = context.loadZone(self.fromZoneType)
        toZone = context.loadZone(self.toZoneType)
        
        for card in fromZone:
            coroutine = context.owner.gainCard(card, fromZone, toZone=toZone)
            try:
                response = yield coroutine.next()
                while True:
                    response = yield coroutine.send(response)
            except StopIteration:
                pass