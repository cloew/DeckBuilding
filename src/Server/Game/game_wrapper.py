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
        
    def toJSON(self, includeActions=False):
        """ Return the game as a JSON Dictionary """
        kicksJSON = GetCardListJSON(self.game.kickDeck, self.game, actions=[{'type':'BUY', 'source':'KICK'}], includeActions=includeActions)
        destroyedJSON = GetCardListJSON(self.game.destroyedDeck, self.game, includeActions=includeActions)
        lineUpJSON = GetCardListJSON(self.game.lineUp.cards, self.game, actions=[{'type':'BUY', 'source':'LINE_UP'}], includeActions=includeActions)
        
        gameJSON = {'id':self.id,
                    'mainDeck':{'count':len(self.game.mainDeck),
                                'hidden':True},
                    'kicks':{'cards':kicksJSON},
                    'destroyed':{'cards':destroyedJSON},
                    'lineUp':lineUpJSON,
                    'turn':TurnWrapper(self.game.currentTurn).toJSON(includeActions=includeActions)}
                    
        if self.game.currentTurn.request is not None:
            gameJSON['request'] = RequestWrapperFactory.buildRequestWrapper(self.game.currentTurn.request, self.game).toJSON()
                    
        return {'game':gameJSON}
                
    def toJSONForPlayer(self, playerId):
        """ Return the more detailed JSON for the given player """
        json = self.toJSON()
        json['you'] = None
        json['players'] = None
        return {'id':self.id,
                'you':PlayerInLobbyWrapper(playerId, self.players[playerId]).toJSON(),
                'players':[PlayerInLobbyWrapper(id, self.players[id]).toJSON() for id in self.players if id != playerId]}