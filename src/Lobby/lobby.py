from Game.game import Game

import random

class Lobby:
    """ Represents the lobby for players wanting to play """
    
    def __init__(self):
        """ Initialize the Lobby """
        self.players = []
        
    def addPlayer(self, player):
        """ Add the player to the game lobby """
        self.players.append(player)
        
    def buildGame(self):
        """ Build the Game """
        players = [player.buildGamePlayer() for player in self.players]
        random.shuffle(players)
        return Game(players)
        