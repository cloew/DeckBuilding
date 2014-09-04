from player import Player
from turn import Turn

from Game.Decks.decks import MainDeckInitializer
from kao_deck.deck import Deck

class Game:
    """ Represents a game of the Deck Building Game """
    LINE_UP_SIZE = 5
    
    def __init__(self, numberOfPlayers):
        """ Initialize the Game """
        self.players = []
        for i in range(numberOfPlayers):
            self.players.append(Player())
            
        self.mainDeck = Deck(deck_initializer=MainDeckInitializer)
        self.mainDeck.shuffle()
        self.lineUp = self.mainDeck.draw(count=self.LINE_UP_SIZE)
        self.weaknessDeck = None
        self.kickDeck = None
        self.destroyedPile = None
        
        self.turnCoroutine = self.pickTurn()
        self.currentTurn = self.turnCoroutine.next()
        
    def pickTurn(self):
        """ Yields the turn for the proper player """
        for player in self.players:
            yield Turn(player)
            
    def __repr__(self):
        """ Return the String Representation of the Game """
        return "<Game: Line-up:{0}>".format(self.lineUp)