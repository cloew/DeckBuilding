from Game.Modes.free_for_all import FreeForAll

class Lobby:
    """ Represents the lobby for players wanting to play """
    
    def __init__(self):
        """ Initialize the Lobby """
        self.players = []
        self.gameMode = FreeForAll()
        self.gameId = None
        
    def addPlayer(self, player):
        """ Add the player to the game lobby """
        self.players.append(player)
        
    def buildGame(self):
        """ Build the Game """
        return self.gameMode.buildGame(self)