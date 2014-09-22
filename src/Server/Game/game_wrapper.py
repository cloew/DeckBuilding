from json_helper import GetCardListJSON
from player_wrapper import PlayerWrapper
from turn_wrapper import TurnWrapper

from Server.Game.Requests.request_wrapper_factory import RequestWrapperFactory

class GameWrapper:
    """ A Wrapper for a Game that handles its conversion to and from JSON """
    
    def __init__(self, id, game, players):
        """ Initialize the Game Wrapper """
        self.id = id
        self.game = game
        self.players = players
        
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
        isYourTurn = self.players[playerId] is self.game.currentTurn.player
        json = self.toJSON(includeActions=isYourTurn)
        json['you'] = PlayerWrapper(self.players[playerId], self.game).toJSONForYourself(includeActions=isYourTurn)
        json['you']['isTurn'] = isYourTurn
        json['players'] = [PlayerWrapper(player, self.game).toJSON(includeActions=isYourTurn) for id, player in self.players.items() if id != playerId]
        return json