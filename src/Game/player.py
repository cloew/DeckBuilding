from Game.Characters.character_factory import CharacterFactory
from Game.Decks.decks import StartingDeckInitializer

from kao_deck.deck_with_discard_pile import DeckWithDiscardPile

class Player:
    """ Represents a Player in the Game """
    HAND_SIZE = 5
    
    def __init__(self):
        """ Initialize a Player """
        self.deck = DeckWithDiscardPile(deck_initializer=StartingDeckInitializer, reshuffle=True)
        self.deck.shuffle()
        self.drawHand()
        self.ongoing = []
        self.character = CharacterFactory.loadCharacter("Batman")
        
    def addOngoing(self, card):
        """ Add the given card as an ongoing effect """
        self.ongoing.append(card)
        
    def drawHand(self):
        """ Draw a new hand """
        self.hand = []
        self.draw(count=self.HAND_SIZE)
        
    def draw(self, count=1):
        """ Draw the given number of cards """
        newCards = self.deck.draw(count=count)
        self.hand += newCards
        
    def gainCard(self, card, fromSource, toSource=None):
        """ Gain the provided card """
        fromSource.remove(card)
        toSource.add(card)
        
    @property
    def discardPile(self):
        """ Return the Deck's Discard Pile """
        return self.deck.discardPile