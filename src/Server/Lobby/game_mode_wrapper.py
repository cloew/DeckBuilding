from Server.Lobby.Settings.deck_setting_wrapper import DeckSettingWrapper

class GameModeWrapper:
    """ Represents a Game Mode and wraps its transformation into JSON """
    
    def __init__(self, gameMode):
        """ Initialize the Game Mode Wrapper """
        self.gameMode = gameMode
        
    def toJSON(self):
        """ Return the JSON for the game mode """
        json = {role:DeckSettingWrapper(self.gameMode.deckSettings[role]).toJSON() for role in self.gameMode.deckSettings}
        json["numberOfVillains"] = {'range':self.gameMode.possibleVillainCounts,
                                    'index':self.gameMode.villainCountIndex}
        return json