
class RemovePlayedCard:
    """ Represents an effect to Remove a specific played card """
    
    def __init__(self, card):
        """ Initialize the Effect with the card to remove from play before discarding """
        self.card = card
        
    def perform(self, context):
        """ Perform the Game Effect """
        if self.card in context.owner.playedCards:
            context.owner.playedCards.remove(self.card)