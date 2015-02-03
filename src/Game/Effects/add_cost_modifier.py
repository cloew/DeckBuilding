from Game.Effects.remove_cost_modifier import RemoveCostModifier

class AddCostModifier:
    """ Represents an effect to Add a Cost Modifier to a Card """
    
    def __init__(self, zoneType, costMod):
        """ Initialize the Effect with the zone to mod the costs for and add the mods """
        self.zoneType = zoneType
        self.costMod = costMod
        
    def perform(self, context):
        """ Perform the Game Effect """
        zone = context.loadZone(self.zoneType)
        removeCostModEffects = []
        for card in zone:
            card.addCostModifier(self.costMod)
            removeEffect = RemoveCostModifier(card, self.costMod)
            removeCostModEffects.append(removeEffect)
            card.onGainEffects.append(removeEffect)
        context.owner.cleanupEffects += removeCostModEffects