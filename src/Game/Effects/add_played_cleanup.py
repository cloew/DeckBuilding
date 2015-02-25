from Game.Effects.cleanup_cards import CleanupCards
from Game.Zones.zone_types import PLAYED

class AddPlayedCleanup:
    """ Effect to allow cleanup effects to modify the played card """
    
    def __init__(self, thenEffects):
        """ Initialize with the effects to perform on cleanup """
        self.thenEffects = thenEffects
        
    def perform(self, context):
        """ Perform the Game Effect """
        context.owner.cleanupEffects.append(CleanupCards([context.parent], PLAYED, self.thenEffects))