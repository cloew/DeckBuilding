from games import games

from card_wrapper import CardWrapper

class GameWrapper:
    """ A Wrapper for a Game that handles its conversion to and from JSON """
    
    def __init__(self, game=None, id=None):
        """ Initialize the Game Wrapper """
        if id is not None:
            game = games[id]
        self.id = id
        self.game = game
        
    def toJSON(self):
        """ Return the game as a JSON Dictionary """
        lineUpJSON = [CardWrapper(card).toJSON() for card in self.game.lineUp]
        
        return {'game':{'id':self.id,
                        'lineUp':lineUpJSON}}