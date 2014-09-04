from Game.Decks.decks import StartingDeckInitializer
from kao_deck.deck_with_discard_pile import DeckWithDiscardPile

class Player:
    """ Represents a Player in the Game """
    HAND_SIZE = 5
    
    def __init__(self):
        """ Initialize a Player """
        self.deck = DeckWithDiscardPile(deck_initializer=StartingDeckInitializer, reshuffle=True)
        self.hand = self.deck.draw(count=self.HAND_SIZE)
        self.ongoing = None