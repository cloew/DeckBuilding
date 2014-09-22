from Game.game import Game

id = 1
games = {}

def StartNewGame():
    """ Start a New Game """
    global games
    global id
    
    game = Game(2)
    currentId = id
    games[currentId] = game
    id += 1
    return currentId