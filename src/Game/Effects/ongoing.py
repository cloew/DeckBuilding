from Game.Effects.remove_played_card import RemovePlayedCard

class Ongoing:
    """ Represents an effect to place the card into the ongoing section """
        
    def perform(self, args):
        """ Perform the Game Effect """
        args.owner.addOngoing(args.parent)
        args.owner.cleanupEffects.append(RemovePlayedCard(args.parent))