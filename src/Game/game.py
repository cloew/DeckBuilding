
class Game:
    """ Represents a game of the Deck Building Game """
    
    def __init__(self):
        """ Initialize the Game """
        self.players = []
        self.mainDeck = None
        self.lineUp = None
        self.weaknessDeck = None
        self.kickDeck = None
        self.destroyedPile = None