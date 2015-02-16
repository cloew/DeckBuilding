from card_id_manager import CardIdManager
from game_over import GameOver
from line_up import LineUp
from player import Player
from supervillain_stack import SuperVillainStack
from turn import Turn

from Game.Commands.start_turn import StartTurn
from Game.Decks.deck_factory import DeckFactory

from Game.Notifications.notification_tracker import NotificationTracker
from Game.Notifications.notification import Notification
from Game.Notifications.notification_types import END_TURN

from Game.Results.game_results import GameResults
from Game.Results.vp_player_results import VPPlayerResults

from kao_deck.deck import Deck

class Game:
    """ Represents a game of the Deck Building Game """
    LINE_UP_SIZE = 5
    
    def __init__(self, players, mainDeck=None, kickDeck=None, weaknessDeck=None, superVillainDeck=None):
        """ Initialize the Game """
        self.players = players
            
        self.mainDeck = mainDeck
        self.kickDeck = kickDeck
        self.weaknessDeck = weaknessDeck
        self.destroyedDeck = Deck()
        self.superVillainStack = SuperVillainStack(superVillainDeck)
        self.cardIdManager = CardIdManager(self)
        self.getCardFromId = self.cardIdManager.getCardFromId
        
        self.lineUp = LineUp(self.mainDeck)
        
        self.gameOver = GameOver(self)
        self.notificationTracker = NotificationTracker()
        
        self.turnCoroutine = self.pickTurn()
        self.nextTurn()
        
        self.isOver = False
        self.results = GameResults(self.players, self, VPPlayerResults)
        self.endAfterTurn = False
        
    def endTurn(self):
        """ End the turn """
        self.currentTurn.cleanup()
        self.notificationTracker.append(Notification(END_TURN, self.currentTurn.player))
        self.lineUp.refill()
        self.superVillainStack.refill()
        
        self.isOver = self.__isOver
        if not self.isOver:
            self.nextTurn()
        else:
            self.end()
            
    def nextTurn(self):
        """ Set the current turn to be the next turn """
        self.currentTurn = self.turnCoroutine.next()
        self.currentTurn.perform(StartTurn(self.currentTurn))
        
    def pickTurn(self):
        """ Yields the turn for the proper player """
        while True:
            for player in self.players:
                yield Turn(player, self)
                
    def end(self):
        """ End the game """
        for player in self.players:
            player.cleanupForEndOfGame()
        self.results.createPlayerResults()
        
    def endAfterThisTurn(self, playersToResultClass):
        """ End the game after this turn """
        self.endAfterTurn = True
        self.results.update(playersToResultClass)
            
    def __repr__(self):
        """ Return the String Representation of the Game """
        return "<Game: Line-up:{0}>".format(self.lineUp)
        
    @property
    def __isOver(self):
        """ Return if the game is Over """
        return self.gameOver.isOver or self.endAfterTurn