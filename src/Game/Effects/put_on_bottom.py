
class PutOnBottom:
    """ Represents an effect to Put a Card on the Bottom """
    
    def __init__(self, fromSourceType, toSourceType, card=None):
        """ Initialize the Effect """
        self.card = card
        self.fromSourceType = fromSourceType
        self.toSourceType = toSourceType
        
    def perform(self, context):
        """ Perform the Game Effect """
        fromSource = context.loadSource(self.fromSourceType)
        toSource = context.loadSource(self.toSourceType)
        
        cards = [self.card]
        if self.card is None:
            cards = list(fromSource)
            
        for card in cards:
            if card in fromSource:
                fromSource.remove(card)
                toSource.putOnBottom(card)