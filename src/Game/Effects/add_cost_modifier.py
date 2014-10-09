from Game.Effects.remove_cost_modifier import RemoveCostModifier

class AddCostModifier:
    """ Represents an effect to Add a Cost Modifier to a Card """
    
    def __init__(self, sourceType, costMod):
        """ Initialize the Effect with the source to mod the costs for and add the mods """
        self.sourceType = sourceType
        self.costMod = costMod
        
    def perform(self, context):
        """ Perform the Game Effect """
        source = context.loadSource(self.sourceType)
        removeCostModEffects = []
        for card in source:
            card.addCostModifier(self.costMod)
            removeEffect = RemoveCostModifier(card, self.costMod)
            removeCostModEffects.append(removeEffect)
            card.onGainEffects.append(removeEffect)
        context.owner.cleanupEffects += removeCostModEffects