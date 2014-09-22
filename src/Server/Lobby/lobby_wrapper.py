from lobbies import lobbies

class LobbyWrapper:
    """ Represents a Lobby and wraps its transformation into JSON """
    
    def __init__(self, id):
        """ Initialize the lobby """
        if id is not None:
            lobby = lobbies[id]
        self.id = id
        self.lobby = lobby
        
    def toJSON(self):
        """ Return the lobby as a JSON Dictionary """
        return {'id':self.id }