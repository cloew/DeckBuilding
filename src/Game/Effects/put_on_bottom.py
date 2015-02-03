
class PutOnBottom:
    """ Represents an effect to Put a Card on the Bottom """
    
    def __init__(self, fromZoneType, toZoneType, card=None):
        """ Initialize the Effect """
        self.card = card
        self.fromZoneType = fromZoneType
        self.toZoneType = toZoneType
        
    def perform(self, context):
        """ Perform the Game Effect """
        fromZone = context.loadZone(self.fromZoneType)
        toZone = context.loadZone(self.toZoneType)
        
        cards = [self.card]
        if self.card is None:
            cards = list(fromZone)
            
        for card in cards:
            if card in fromZone:
                fromZone.remove(card)
                toZone.putOnBottom(card)