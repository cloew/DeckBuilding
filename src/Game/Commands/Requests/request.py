
class Request:
    """ Represents a Request for additional information """
    
    def __init__(self, players):
        """ Initialize the request with the players it should request from """
        self.players = players