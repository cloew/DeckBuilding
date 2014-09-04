from player import Player
from turn import Turn

class Game:
    """ Represents a game of the Deck Building Game """
    
    def __init__(self, numberOfPlayers):
        """ Initialize the Game """
        self.players = []
        for i in range(numberOfPlayers):
            self.players.append(Player())
            
        self.mainDeck = None
        self.lineUp = None
        self.weaknessDeck = None
        self.kickDeck = None
        self.destroyedPile = None
        
        self.turnCoroutine = self.pickTurn()
        self.currentTurn = self.turnCoroutine.next()
        
    def pickTurn(self):
        """ Yields the turn for the proper player """
        for player in self.players:
            yield Turn(player)