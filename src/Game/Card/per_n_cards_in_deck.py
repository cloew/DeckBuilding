from Game.Sources.source_types import DECK

class PerNCardsInDeck:
    """ Represents a VP based on the number of cards in your deck """
    
    def __init__(self, number):
        """ Initialize the points calculator with the number of cards to award points for """
        self.number = number
        
    def calculatePoints(self, context):
        """ Return the number of Points """
        deck = context.loadSource(DECK)
        return len(deck)/self.number