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
        players = self.getGamePlayers()
        return Game(players)
        
    def getGamePlayers(self):
        """ Return the Game Players in their proper order """
        players = [player.buildGamePlayer() for player in self.players]
        firstPlayers = [player for player in players if player.goesFirst]
        otherPlayers = [player for player in players if not player.goesFirst]
        
        random.shuffle(firstPlayers)
        random.shuffle(otherPlayers)
        
        return firstPlayers + otherPlayers