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
        self.chosenDecks = {role:self.potentialDecks[role][0] for role in requiredRoles}
        
        self.villainCountIndex = 0
        self.possibleVillainCounts = self.getVillainCountRange()
        
    def buildGame(self, lobby):
        """ Build the Game """
        players = self.getGamePlayers(lobby)
        return Game(players, mainDeck=DeckFactory.load(self.mainDeckId).loadDeck(),
                             kickDeck=DeckFactory.load(self.kickDeckId).loadDeck(),
                             weaknessDeck=DeckFactory.load(self.weaknessDeckId).loadDeck(),
                             superVillainDeck=DeckFactory.load(self.supervillainDeckId).loadDeck(number=self.numberOfVillains))
        
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
        index = index % len(self.potentialDecks[role])
        self.chosenDecks[role] = self.potentialDecks[role][index]
        
    def setNumberOfVillains(self, index):
        """ Set the number of villains to play against """
        self.villainCountIndex = index
        
    def getVillainCountRange(self):
        """ Get the possible counts for the number of villains """
        return range(8, len(DeckFactory.load(self.supervillainDeckId).loadDeck())+1)
        
    @property
    def mainDeckId(self):
        """ Return the chosen main deck id """
        return self.chosenDecks[MAIN]
        
    @property
    def kickDeckId(self):
        """ Return the chosen kick deck id """
        return self.chosenDecks[KICK]
        
    @property
    def weaknessDeckId(self):
        """ Return the chosen weakness deck id """
        return self.chosenDecks[WEAKNESS]
        
    @property
    def supervillainDeckId(self):
        """ Return the chosen supervillain deck id """
        return self.chosenDecks[SUPERVILLAIN]
        
    @property
    def numberOfVillains(self):
        """ Return the number of supervillains to play with """
        return self.possibleVillainCounts[self.villainCountIndex]