
class AddCostModifier:
    """ Represents an effect to Add a Cost Modifier to a Card """
    
    def __init__(self, sourceType, costMod):
        """ Initialize the Effect with the source to mod the costs for and add the mods """
        self.sourceType = sourceType
        self.costMod = costMod
        
    def perform(self, context):
        """ Perform the Game Effect """
        source = context.loadSource(self.sourceType)
        for card in source:
            card.addCostModifier(self.costMod)