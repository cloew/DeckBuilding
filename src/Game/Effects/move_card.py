
class MoveCard:
    """ Represents an effect to Move a Card """
    
    def __init__(self, fromSourceType, toSourceType):
        """ Initialize the Effect """
        self.fromSourceType = fromSourceType
        self.toSourceType = toSourceType
        
    def perform(self, context):
        """ Perform the Game Effect """
        fromSource = context.loadSource(self.fromSourceType)
        toSource = context.loadSource(self.toSourceType)
        
        for card in list(fromSource):
            fromSource.remove(card)
            toSource.add(card)