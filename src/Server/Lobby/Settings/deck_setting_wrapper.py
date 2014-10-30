from Game.Decks.deck_roles import MAIN, KICK, WEAKNESS, SUPERVILLAIN, STARTER

class DeckSettingWrapper:
    """ Represents a Game Mode and wraps its transformation into JSON """
    
    def __init__(self, deckSetting):
        """ Initialize the Deck Setting Wrapper """
        self.deckSetting = deckSetting
        
    def toJSON(self):
        """ Return the JSON for the game mode """
        return {"options":self.deckSetting.potentialDeckIds,
                "current":self.deckSetting.index}