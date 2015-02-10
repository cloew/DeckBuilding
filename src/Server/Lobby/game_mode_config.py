from kao_json import JsonConfig, JsonAttr
from Game.Modes.free_for_all import FreeForAll

class GameModeConfig(JsonConfig):
    """ Represents the Json Config for the Game Mode """
    
    def __init__(self):
        """ Initialize the Game Mode Config """
        JsonConfig.__init__(self, FreeForAll, [JsonAttr('numberOfVillains', lambda gameMode: {'range':gameMode.possibleVillainCounts, 'index':gameMode.villainCountIndex})])
        
    def getAttrs(self, gameMode, classToConfig):
        """ Return the attributes for the Configuration """
        attrs = JsonConfig.getAttrs(self, gameMode, classToConfig)
        return attrs + [JsonAttr(role, self.getDeckSettingByRole(role)) for role in gameMode.deckSettings]
        
    def getDeckSettingByRole(self, role):
        def getDeckSetting(gameMode):
            return gameMode.deckSettings[role]
        return getDeckSetting