from Game.Effects.remove_played_card import RemovePlayedCard

class Ongoing:
    """ Represents an effect to place the card into the ongoing section """
        
    def perform(self, context):
        """ Perform the Game Effect """
        context.owner.addOngoing(context.parent)
        context.owner.cleanupEffects.append(RemovePlayedCard(context.parent))