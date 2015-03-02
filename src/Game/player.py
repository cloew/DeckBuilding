from Game.Characters.character_factory import CharacterFactory
from Game.Context.player_context import PlayerContext
from Game.Effects.effect_runner import PerformEffects
from Game.Events.cards_event import CardsEvent

class Player:
    """ Represents a Player in the Game """
    STANDARD_HAND_SIZE = 5
    
    def __init__(self, name, character, startingDeck):
        """ Initialize a Player """
        self.name = name
        self.character = character
        
        self.nextHandSize = self.STANDARD_HAND_SIZE
        self.deck = startingDeck
        self.drawHand()
        self.ongoing = []
        self.underCharacter = []
        
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
        context = PlayerContext(game, None, player=self)
        return sum([card.calculatePoints(context) for card in self.deck])
        
    def moveToDeck(self, otherList):
        """ Move a card from the other list to the deck """
        self.deck.add(otherList)
        del otherList[:]
        
    def addStartingEffects(self, addOngoingEffects):
        """ Add Starting Effects for the current player """
        for card in self.ongoing:
            addOngoingEffects(card)
        self.character.addOngoingEffects(addOngoingEffects)
        
    def addOutOfTurnEffects(self, addOngoingEffects):
        """ Add Starting Effects for the current player """
        self.character.addOutOfTurnEffects(addOngoingEffects)
        
    @property
    def discardPile(self):
        """ Return the Deck's Discard Pile """
        return self.deck.discardPile
        
    @property
    def goesFirst(self):
        """ Return whether the Player should go first """
        return self.character.goesFirst