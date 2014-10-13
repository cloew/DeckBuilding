from Game.game import Game
from Game.Decks.deck_factory import DeckFactory

import random

class FreeForAll:
    """ Represents the Free For All Game Mode """
        
    def buildGame(self, lobby):
        """ Build the Game """
        players = self.getGamePlayers(lobby)
        return Game(players, mainDeck=DeckFactory.load("Deck 1").loadDeck(),
                             kickDeck=DeckFactory.load("Kick").loadDeck(),
                             weaknessDeck=DeckFactory.load("Weakness").loadDeck(),
                             superVillainDeck=DeckFactory.load("Super Villains").loadDeck())
        
    def getGamePlayers(self, lobby):
        """ Return the Game Players in their proper order """
        players = [player.buildGamePlayer() for player in lobby.players]
        firstPlayers = [player for player in players if player.goesFirst]
        otherPlayers = [player for player in players if not player.goesFirst]
        
        random.shuffle(firstPlayers)
        random.shuffle(otherPlayers)
        
        return firstPlayers + otherPlayers