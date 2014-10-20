from Game.game import Game
from Game.Decks.deck_factory import DeckFactory
from Game.Decks.deck_roles import MAIN, KICK, WEAKNESS, SUPERVILLAIN, STARTER

import random

class FreeForAll:
    """ Represents the Free For All Game Mode """
    
    def __init__(self):
        """ Initialize the Free For All Game Mode """
        requiredRoles = [MAIN, KICK, WEAKNESS, SUPERVILLAIN]
        self.potentialDecks = {role:DeckFactory.findDeckIdsToFillRole(role) for role in requiredRoles}
        
        
        self.mainDeckId = self.potentialDecks[MAIN][0]
        self.kickDeckId = self.potentialDecks[KICK][0]
        self.weaknessDeckId = self.potentialDecks[WEAKNESS][0]
        self.supervillainDeckId = self.potentialDecks[SUPERVILLAIN][0]
        
    def buildGame(self, lobby):
        """ Build the Game """
        players = self.getGamePlayers(lobby)
        return Game(players, mainDeck=DeckFactory.load(self.mainDeckId).loadDeck(),
                             kickDeck=DeckFactory.load(self.kickDeckId).loadDeck(),
                             weaknessDeck=DeckFactory.load(self.weaknessDeckId).loadDeck(),
                             superVillainDeck=DeckFactory.load(self.supervillainDeckId).loadDeck())
        
    def getGamePlayers(self, lobby):
        """ Return the Game Players in their proper order """
        players = [player.buildGamePlayer() for player in lobby.players]
        firstPlayers = [player for player in players if player.goesFirst]
        otherPlayers = [player for player in players if not player.goesFirst]
        
        random.shuffle(firstPlayers)
        random.shuffle(otherPlayers)
        
        return firstPlayers + otherPlayers