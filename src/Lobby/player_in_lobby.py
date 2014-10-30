from Game.player import Player
from Game.Characters.character_factory import CharacterFactory
from Game.Decks.deck_roles import STARTING

from Lobby.Settings.deck_setting import DeckSetting

class PlayerInLobby:
    """ Represents a Player In the Lobby """
    
    def __init__(self):
        """ Initialize the Player """
        self.setName("")
        self.setCharacter("Green Lantern")
        self.startingDeckSetting = DeckSetting(STARTING)
        
    def buildGamePlayer(self):
        """ Build the Game Player for this player in the Lobby """
        self.player = Player(self.name, self.character, self.startingDeckSetting.loadDeck())
        return self.player
        
    def setName(self, name):
        """ Set the current Player's Name """
        self.name = name
        
    def setCharacter(self, characterName):
        """ Set the current Player's Character """
        self.character = CharacterFactory.load(characterName)