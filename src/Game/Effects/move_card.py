
class MoveCard:
    """ Represents an effect to Move a Card """
    
    def __init__(self, fromZoneType, toZoneType):
        """ Initialize the Effect """
        self.fromZoneType = fromZoneType
        self.toZoneType = toZoneType
        
    def perform(self, context):
        """ Perform the Game Effect """
        fromZone = context.loadZone(self.fromZoneType)
        toZone = context.loadZone(self.toZoneType)
        self.moveCards(fromZone, toZone)
        
    def moveCards(self, fromZone, toZone):
        for card in list(fromZone):
            fromZone.remove(card)
            toZone.add(card)