from card_wrapper import CardWrapper
from json_helper import GetCardListJSON
from player_wrapper import PlayerWrapper
from supervillain_stack_wrapper import SuperVillainStackWrapper
from turn_wrapper import TurnWrapper

from Game.Sources.source_factory import KICK, LINE_UP
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
        kicksJSON = GetCardListJSON(self.game.kickDeck, self.game, actions=[{'type':'BUY', 'source':KICK}], includeActions=includeActions)
        weaknessesJSON = GetCardListJSON(self.game.weaknessDeck, self.game, includeActions=includeActions)
        destroyedJSON = GetCardListJSON(self.game.destroyedDeck, self.game, includeActions=includeActions)
        lineUpJSON = GetCardListJSON(self.game.lineUp.cards, self.game, actions=[{'type':'BUY', 'source':LINE_UP}], includeActions=includeActions)
        
        gameJSON = {'id':self.id,
                    'isOver':self.game.isOver,
                    'mainDeck':{'count':len(self.game.mainDeck),
                                'hidden':True},
                    'superVillains':SuperVillainStackWrapper(self.game.superVillainStack).toJSON(includeActions=includeActions),
                    'kicks':{'cards':kicksJSON, 'count':len(kicksJSON)},
                    'weaknesses':{'cards':weaknessesJSON, 'count':len(weaknessesJSON)},
                    'destroyed':{'cards':destroyedJSON, 'count':len(destroyedJSON)},
                    'lineUp':lineUpJSON,
                    'turn':TurnWrapper(self.game.currentTurn).toJSON(includeActions=includeActions)}
                    
        return {'game':gameJSON}
                
    def toJSONForPlayer(self, playerId):
        """ Return the more detailed JSON for the given player """
        yourPlayer = self.players[playerId]
        isYourTurn = yourPlayer is self.game.currentTurn.player
        json = self.toJSON(includeActions=isYourTurn)
        gameJSON = json['game']
        gameJSON['you'] = PlayerWrapper(yourPlayer, self.game).toJSONForYourself(includeActions=isYourTurn)
        gameJSON['you']['isTurn'] = isYourTurn
        gameJSON['players'] = [PlayerWrapper(player, self.game).toJSON(includeActions=isYourTurn) for id, player in self.players.items() if id != playerId]
                    
        request = self.game.currentTurn.request
        if request is not None and yourPlayer in request.players:
            gameJSON['request'] = RequestWrapperFactory.buildRequestWrapper(self.game.currentTurn.request, self.game).toJSON(includeActions=True)
        return json
                
    def toResultJSONForPlayer(self, playerId):
        """ Return the more detailed JSON for the given player """
        yourPlayer = self.players[playerId]
        json = {}
        json['you'] = {'points':yourPlayer.calculatePoints(self.game)}
        json['players'] = [{'points':player.calculatePoints(self.game)} for id, player in self.players.items() if id != playerId]
        return json