from Game.player import Player
from Game.Characters.character_factory import CharacterFactory
from Game.Decks.deck_factory import DeckFactory

class PlayerInLobby:
    """ Represents a Player In the Lobby """
    
    def __init__(self):
        """ Initialize the Player """
        self.setName("")
        self.setCharacter("Green Lantern")
        
    def buildGamePlayer(self):
        """ Build the Game Player for this player in the Lobby """
        self.player = Player(self.name, self.character, DeckFactory.load("Deck 1 - Starting").loadDeck())
        return self.player
        
    def setName(self, name):
        """ Set the current Player's Name """
        self.name = name
        
    def setCharacter(self, characterName):
        """ Set the current Player's Character """
        self.character = CharacterFactory.load(characterName)