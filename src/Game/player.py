from Game.Characters.character_factory import CharacterFactory
from Game.Decks.decks import StartingDeckInitializer
from Game.Effects.effect_arguments import EffectArguments

from kao_deck.deck_with_discard_pile import DeckWithDiscardPile

class Player:
    """ Represents a Player in the Game """
    STANDARD_HAND_SIZE = 5
    
    def __init__(self, character):
        """ Initialize a Player """
        self.nextHandSize = self.STANDARD_HAND_SIZE
        self.deck = DeckWithDiscardPile(deck_initializer=StartingDeckInitializer, reshuffle=True)
        self.deck.shuffle()
        self.drawHand()
        self.ongoing = []
        self.character = character
        
    def addOngoing(self, card):
        """ Add the given card as an ongoing effect """
        self.ongoing.append(card)
        
    def drawHand(self):
        """ Draw a new hand """
        self.hand = []
        self.draw(count=self.nextHandSize)
        self.nextHandSize = self.STANDARD_HAND_SIZE
        
    def draw(self, count=1):
        """ Draw the given number of cards """
        newCards = self.deck.draw(count=count)
        self.hand += newCards
        
    def gainCard(self, card, fromSource, toSource=None):
        """ Gain the provided card """
        fromSource.remove(card)
        toSource.add(card)
        
    def modifyHandSize(self, change):
        """ Modify the Player's Next Hand Size """
        self.nextHandSize += change
        
    def cleanupForEndOfGame(self):
        """ Cleanup the Player so they have all their cards in their deck """
        self.moveToDeck(self.ongoing)
        self.moveToDeck(self.hand)
        self.deck.shuffleInDiscardPile()
        
    def calculatePoints(self, game):
        """ Calculate the Player's Victory Points """
        args = EffectArguments(game, None, player=self)
        return sum([card.calculatePoints(args) for card in self.deck])
        
    def moveToDeck(self, otherList):
        """ Move a card from the other list to the deck """
        self.deck.add(otherList)
        del otherList[:]
        
    @property
    def discardPile(self):
        """ Return the Deck's Discard Pile """
        return self.deck.discardPile