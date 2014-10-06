from game_over import GameOver
from line_up import LineUp
from player import Player
from supervillain_stack import SuperVillainStack
from turn import Turn

from Game.Commands.start_turn import StartTurn
from Game.Decks.decks import MainDeckInitializer, KickDeckInitializer, WeaknessDeckInitializer, SuperVillainDeckInitializer
from Game.Notifications.notification_tracker import NotificationTracker

from kao_deck.deck import Deck

class Game:
    """ Represents a game of the Deck Building Game """
    LINE_UP_SIZE = 5
    
    def __init__(self, players):
        """ Initialize the Game """
        self.players = players
            
        self.mainDeck = Deck(deck_initializer=MainDeckInitializer)
        self.mainDeck.shuffle()
        self.lineUp = LineUp(self.mainDeck)
        self.kickDeck = Deck(deck_initializer=KickDeckInitializer)
        self.weaknessDeck = Deck(deck_initializer=WeaknessDeckInitializer)
        self.destroyedDeck = Deck()
        self.superVillainStack = SuperVillainStack(Deck(deck_initializer=SuperVillainDeckInitializer))
        
        self.gameOver = GameOver(self)
        self.notificationTracker = NotificationTracker()
        
        self.turnCoroutine = self.pickTurn()
        self.nextTurn()
        self.isOver = False
        
    def endTurn(self):
        """ End the turn """
        self.currentTurn.cleanup()
        self.lineUp.refill()
        self.superVillainStack.refill()
        self.isOver = self.gameOver.isOver
        if not self.isOver:
            self.nextTurn()
        else:
            for player in self.players:
                player.cleanupForEndOfGame()
            
    def nextTurn(self):
        """ Set the current turn to be the next turn """
        self.currentTurn = self.turnCoroutine.next()
        self.currentTurn.perform(StartTurn(self.currentTurn))
        
    def pickTurn(self):
        """ Yields the turn for the proper player """
        while True:
            for player in self.players:
                yield Turn(player, self)
            
    def __repr__(self):
        """ Return the String Representation of the Game """
        return "<Game: Line-up:{0}>".format(self.lineUp)