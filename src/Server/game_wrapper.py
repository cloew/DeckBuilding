from games import games

class GameWrapper:
    """ A Wrapper for a Word Guess Game that handles its conversion to and from JSON """
    
    def __init__(self, game=None, id=None):
        """ Initialize the Game Wrapper """
        if id is not None:
            game = games[id]
        self.game = game
        
    def guess(self, guesses):
        """ Return the results of the guess """
        self.game.guess(guesses)
        
    def startNextRound(self):
        """ Start the Next Round """
        self.game.startNextRound()
        
    def toJSON(self):
        """ Return the game as a JSON Dictionary """
        guesses = [{'results':[{'guess': charResult.guessChar, 'result':charResult.result} for charResult in result.results]} for result in self.game.currentRound.guesses]
        return {'game':{'id':self.game.id,
                        'points':self.game.points,
                        'wordLength':self.game.currentRound.wordLength,
                        'triesLeft':self.game.currentRound.triesLeft,
                        'roundComplete':self.game.currentRound.completed,
                        'hasNextRound':self.game.hasNextRound(),
                        'guesses':guesses}}