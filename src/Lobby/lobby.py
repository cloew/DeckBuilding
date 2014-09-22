
class Lobby:
    """ Represents the lobby for players wanting to play """
    
    def __init__(self):
        """ Initialize the Lobby """
        self.players = []
        
    def addPlayer(self, player):
        """ Add the plyaere to the game lobby """
        self.players.append(player)