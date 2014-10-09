
class RemoveCostModifier:
    """ Represents an effect to Remove a Cost Modifier to a Card """
    
    def __init__(self, card, costMod):
        """ Initialize the Effect with the Card and the Mod to remove """
        self.card = card
        self.costMod = costMod
        
    def perform(self, context):
        """ Perform the Game Effect """
        self.card.removeCostModifier(self.costMod)