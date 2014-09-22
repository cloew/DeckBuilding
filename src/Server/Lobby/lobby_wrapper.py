from Lobby.player_in_lobby import PlayerInLobby
from Server.Game.games import StartNewGame
from Server.Lobby.player_in_lobby_wrapper import PlayerInLobbyWrapper

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
            
    def startGame(self):
        """ Start the game the lobby is for """
        game = self.lobby.buildGame()
        return StartNewGame(game=game)
        
    def toJSON(self):
        """ Return the lobby as a JSON Dictionary """
        return {'id':self.id,
                'players':[PlayerInLobbyWrapper(id, self.players[id]).toJSON() for id in self.players]}
                
    def toJSONForPlayer(self, playerId):
        """ Return the more detailed JSON for the given player """
        return {'id':self.id,
                'you':PlayerInLobbyWrapper(playerId, self.players[playerId]).toJSON(),
                'players':[PlayerInLobbyWrapper(id, self.players[id]).toJSON() for id in self.players if id != playerId]}