
class RemovePlayedCard:
    """ Represents an effect to Remove a specific played card """
    
    def __init__(self, card):
        """ Initialize the Effect with the card to remove from play before discarding """
        self.card = card
        
    def perform(self, owner):
        """ Perform the Game Effect """
        owner.playedCards.remove(self.card)