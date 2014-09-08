from line_up import LineUp
from player import Player
from turn import Turn

from Game.Decks.decks import MainDeckInitializer, KickDeckInitializer
from Game.Events.game_event_listener import GameEventListener

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
        self.lineUp = LineUp(self.mainDeck)
        self.weaknessDeck = None
        self.kickDeck = Deck(deck_initializer=KickDeckInitializer)
        self.destroyedPile = None
        
        self.eventListener = GameEventListener()
        
        self.turnCoroutine = self.pickTurn()
        self.nextTurn()
        
    def endTurn(self):
        """ End the turn """
        self.currentTurn.cleanup()
        self.lineUp.refill()
        self.nextTurn()
            
    def nextTurn(self):
        """ Set the current turn to be the next turn """
        self.currentTurn = self.turnCoroutine.next()
        
    def pickTurn(self):
        """ Yields the turn for the proper player """
        while True:
            for player in self.players:
                yield Turn(player, self)
            
    def __repr__(self):
        """ Return the String Representation of the Game """
        return "<Game: Line-up:{0}>".format(self.lineUp)