from Game.Decks.deck_roles import MAIN, KICK, WEAKNESS, SUPERVILLAIN, STARTER

class GameModeWrapper:
    """ Represents a Game Mode and wraps its transformation into JSON """
    
    def __init__(self, gameMode):
        """ Initialize the Game Mode Wrapper """
        self.gameMode = gameMode
        
    def toJSON(self):
        """ Return the JSON for the game mode """
        return {MAIN:{"options":self.gameMode.potentialDecks[MAIN],
                      "current":self.gameMode.potentialDecks[MAIN].index(self.gameMode.mainDeckId)},
                KICK:{"options":self.gameMode.potentialDecks[KICK],
                      "current":self.gameMode.potentialDecks[KICK].index(self.gameMode.kickDeckId)},
                WEAKNESS:{"options":self.gameMode.potentialDecks[WEAKNESS],
                          "current":self.gameMode.potentialDecks[WEAKNESS].index(self.gameMode.weaknessDeckId)},
                SUPERVILLAIN:{"options":self.gameMode.potentialDecks[SUPERVILLAIN],
                              "current":self.gameMode.potentialDecks[SUPERVILLAIN].index(self.gameMode.supervillainDeckId)}}