from helpers.incrementer import Incrementer

gameIdProvider = Incrementer(startAt=1)
games = {}
gameToPlayers = {}

def StartNewGame(game, players):
    """ Start a New Game """
    global games
        
    currentId = gameIdProvider.next()
    games[currentId] = game
    gameToPlayers[currentId] = players
    return currentId