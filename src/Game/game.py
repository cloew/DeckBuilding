from player import Player

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