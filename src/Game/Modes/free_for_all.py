from Game.game import Game
from Game.Decks.deck_factory import DeckFactory
from Game.Decks.deck_roles import MAIN, KICK, WEAKNESS, SUPERVILLAIN, STARTER
from Lobby.Settings.deck_setting import DeckSetting

import random

class FreeForAll:
    """ Represents the Free For All Game Mode """
    
    def __init__(self):
        """ Initialize the Free For All Game Mode """
        requiredRoles = [MAIN, KICK, WEAKNESS, SUPERVILLAIN]
        self.deckSettings = {role:DeckSetting(role) for role in requiredRoles}
        
        self.villainCountIndex = 0
        self.possibleVillainCounts = self.getVillainCountRange()
        
    def buildGame(self, lobby):
        """ Build the Game """
        players = self.getGamePlayers(lobby)
        return Game(players, mainDeck=self.mainDeck,
                             kickDeck=self.kickDeck,
                             weaknessDeck=self.weaknessDeck,
                             superVillainDeck=self.loadSupervillainDeck(number=self.numberOfVillains))
        
    def getGamePlayers(self, lobby):
        """ Return the Game Players in their proper order """
        players = [player.buildGamePlayer() for player in lobby.players]
        firstPlayers = [player for player in players if player.goesFirst]
        otherPlayers = [player for player in players if not player.goesFirst]
        
        random.shuffle(firstPlayers)
        random.shuffle(otherPlayers)
        
        return firstPlayers + otherPlayers
        
    def setDeckForRole(self, role, index):
        """ Set the deck for the given role """
        self.deckSettings[role].setDeck(index)
        
    def setNumberOfVillains(self, index):
        """ Set the number of villains to play against """
        if index < 0:
            self.villainCountIndex = len(self.possibleVillainCounts)+index
        else:
            self.villainCountIndex = index % len(self.possibleVillainCounts)
        
    def getVillainCountRange(self):
        """ Get the possible counts for the number of villains """
        return range(8, len(self.loadSupervillainDeck())+1)
        
    @property
    def mainDeck(self):
        """ Return the chosen main deck """
        return self.deckSettings[MAIN].loadDeck()
        
    @property
    def kickDeck(self):
        """ Return the chosen kick deck """
        return self.deckSettings[KICK].loadDeck()
        
    @property
    def weaknessDeck(self):
        """ Return the chosen weakness deck """
        return self.deckSettings[WEAKNESS].loadDeck()
        
    def loadSupervillainDeck(self, **kwargs):
        """ Return the chosen supervillain deck id """
        return self.deckSettings[SUPERVILLAIN].loadDeck(**kwargs)
        
    @property
    def numberOfVillains(self):
        """ Return the number of supervillains to play with """
        return self.possibleVillainCounts[self.villainCountIndex]