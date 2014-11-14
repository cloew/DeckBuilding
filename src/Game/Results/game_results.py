
class GameResults:
    """ Represents the results for a game """
    
    def __init__(self, playerResults):
        """ Initialize the Game Results with the results for each player """
        self.playerResults = playerResults
        self.playerResults.sort()