from game_wrapper import GameWrapper

id = 1
games = {}

def StartNewGame(game, players):
    """ Start a New Game """
    global games
    global id
        
    currentId = id
    games[currentId] = GameWrapper(currentId, game, players)
    id += 1
    return currentId