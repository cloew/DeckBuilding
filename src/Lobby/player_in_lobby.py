from Game.player import Player
from Game.Characters.character_factory import CharacterFactory

class PlayerInLobby:
    """ Represents a Player In the Lobby """
    
    def __init__(self):
        """ Initialize the Player """
        self.name = ""
        self.setCharacter("Green Lantern")
        
    def buildGamePlayer(self):
        """ Build the Game Player for this player in the Lobby """
        self.player = Player(self.name, self.character)
        return self.player
        
    def setCharacter(self, characterName):
        """ Set the current Player's Character """
        self.character = CharacterFactory.load(characterName)