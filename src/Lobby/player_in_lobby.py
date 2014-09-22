from Game.player import Player

class PlayerInLobby:
    """ Represents a Player In the Lobby """
    
    def __init__(self):
        """ Initialize the Player """
        self.character = None
        
    def buildGamePlayer(self):
        """ Build the Game Player for this player in the Lobby """
        return Player()