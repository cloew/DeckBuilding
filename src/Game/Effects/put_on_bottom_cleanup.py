from Game.Effects.put_on_bottom import PutOnBottom
from Game.Sources.source_factory import PLAYED, DECK

class PutOnBottomCleanup:
    """ Represents an effect to place the card on the Bottom of the deck instead of the Discard Pile """
        
    def perform(self, args):
        """ Perform the Game Effect """
        args.owner.cleanupEffects.append(PutOnBottom(args.parent, PLAYED, DECK))