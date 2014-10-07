from Game.Effects.put_on_bottom import PutOnBottom
from Game.Sources.source_types import PLAYED, DECK

class PutOnBottomCleanup:
    """ Represents an effect to place the card on the Bottom of the deck instead of the Discard Pile """
        
    def perform(self, context):
        """ Perform the Game Effect """
        context.owner.cleanupEffects.append(PutOnBottom(PLAYED, DECK, card=context.parent))