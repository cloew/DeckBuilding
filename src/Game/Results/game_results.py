
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