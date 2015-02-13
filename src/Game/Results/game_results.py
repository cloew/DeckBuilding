
class GameResults:
    """ Represents the results for a game """
    
    def __init__(self, players, game, defaultResultsClass):
        """ Initialize the Game Results with the results for each player """
        self.playerToResultClass = {player:defaultResultsClass for player in players}
        self.game = game
        self.playerResults = []
        self.update = self.playerToResultClass.update
        
    def createPlayerResults(self):
        self.playerResults = [self.playerToResultClass[player](player, self.game) for player in self.playerToResultClass]
        self.playerResults.sort()
        self.setPlayerRanks()
        
    def setPlayerRanks(self):
        """ Set the player's game ranking (1st, 2nd, 3rd, ...) """
        previousPlayer = None
        previousRank = 0
        for playerResults in self.playerResults:
            if previousPlayer is None or playerResults < previousPlayer:
                previousRank += 1
                playerResults.rank = previousRank
                previousPlayer = playerResults
            else:
                playerResults.rank = previousRank