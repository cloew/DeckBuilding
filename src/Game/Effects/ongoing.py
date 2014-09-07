from Game.Effects.remove_played_card import RemovePlayedCard

class Ongoing:
    """ Represents an effect to place the card into the ongoing section """
        
    def perform(self, owner, card):
        """ Perform the Game Effect """
        owner.addOngoing(card)
        owner.cleanupEffects.append(RemovePlayedCard(card))