id = 1
games = {}
gameToPlayers = {}

def StartNewGame(game, players):
    """ Start a New Game """
    global games
    global id
        
    currentId = id
    games[currentId] = game
    gameToPlayers[currentId] = players
    id += 1
    return currentId