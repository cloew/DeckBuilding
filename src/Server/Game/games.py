from Game.game import Game
from Game.player import Player

id = 1
games = {}

def StartNewGame(game=None):
    """ Start a New Game """
    global games
    global id
    
    if game is None:
        game = Game([Player()])
        
    currentId = id
    games[currentId] = game
    id += 1
    return currentId