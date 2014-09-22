from Lobby.lobby import Lobby

id = 1
lobbies = {}

def StartNewLobby():
    """ Start a New Lobby """
    global lobbies
    global id
    
    lobby = Lobby()
    currentId = id
    lobbies[currentId] = lobby
    id += 1
    return currentId