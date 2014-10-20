from Game.Characters.character_factory import CharacterFactory
from Game.Decks.deck_factory import DeckFactory
from Game.Effects.game_contexts import PlayerContext
from Game.Effects.effect_runner import PerformEffects
from Game.Events.cards_event import CardsEvent

class Player:
    """ Represents a Player in the Game """
    STANDARD_HAND_SIZE = 5
    
    def __init__(self, name, character):
        """ Initialize a Player """
        self.name = name
        self.character = character
        
        self.nextHandSize = self.STANDARD_HAND_SIZE
        self.deck = DeckFactory.load("Deck 1 - Starting").loadDeck()
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
        
    def gainCard(self, card, fromSource, toSource=None, game=None):
        """ Gain the provided card """
        fromSource.remove(card)
        toSource.add(card)
        event = CardsEvent([card], toSource, PlayerContext(game, card, player=self))
        coroutine = PerformEffects(card.onGainEffects, event.context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)
        
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
        
    @property
    def discardPile(self):
        """ Return the Deck's Discard Pile """
        return self.deck.discardPile
        
    @property
    def goesFirst(self):
        """ Return whether the Player should go first """
        return self.character.goesFirst