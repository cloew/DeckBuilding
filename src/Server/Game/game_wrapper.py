from games import games

from json_helper import GetCardListJSON
from turn_wrapper import TurnWrapper

from Server.Game.Requests.request_wrapper_factory import RequestWrapperFactory

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
        kicksJSON = GetCardListJSON(self.game.kickDeck, actions=[{'type':'BUY', 'source':'KICK'}])
        destroyedJSON = GetCardListJSON(self.game.destroyedDeck)
        lineUpJSON = GetCardListJSON(self.game.lineUp.cards, actions=[{'type':'BUY', 'source':'LINE_UP'}])
        
        gameJSON = {'id':self.id,
                    'mainDeck':{'count':len(self.game.mainDeck),
                                'hidden':True},
                    'kicks':{'cards':kicksJSON},
                    'destroyed':{'cards':destroyedJSON},
                    'lineUp':lineUpJSON,
                    'turn':TurnWrapper(self.game.currentTurn).toJSON()}
                    
        if self.game.currentTurn.request is not None:
            gameJSON['request'] = RequestWrapperFactory.buildRequestWrapper(self.game.currentTurn.request).toJSON()
                    
        return {'game':gameJSON}