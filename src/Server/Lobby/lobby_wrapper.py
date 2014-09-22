from Lobby.player_in_lobby import PlayerInLobby

class LobbyWrapper:
    """ Represents a Lobby and wraps its transformation into JSON """
    
    def __init__(self, id, lobby):
        """ Initialize the lobby """
        self.id = id
        self.lobby = lobby
        self.players = {}
        self.playerIdProvider = self.getPlayerId()
        
    def addPlayer(self):
        """ Add a player to the Lobby """
        playerId = self.playerIdProvider.next()
        player = PlayerInLobby()
        self.players[playerId] = player
        self.lobby.addPlayer(player)
        return playerId
        
    def getPlayerId(self):
        """ Return the next player Id """
        id = 1
        while True:
            yield id
            id += 1
        
    def toJSON(self):
        """ Return the lobby as a JSON Dictionary """
        return {'id':self.id }