from Server.Json.character_wrapper import CharacterWrapper
from Server.Lobby.Settings.deck_setting_wrapper import DeckSettingWrapper

class PlayerInLobbyWrapper:
    """ Represents a Player in a Lobby and wraps its transformation into JSON """
    
    def __init__(self, id, player):
        """ Initialize the Player """
        self.id = id
        self.player = player
        
    def toJSON(self):
        """ Return the lobby as a JSON Dictionary """
        return {'id':self.id,
                'name':self.player.name,
                'character':CharacterWrapper(self.player.character).toJSON(),
                'starting':DeckSettingWrapper(self.player.startingDeckSetting).toJSON()}