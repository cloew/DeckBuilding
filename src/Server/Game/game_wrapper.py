from card_wrapper import CardWrapper
from json_helper import GetCardListJSON
from player_wrapper import PlayerWrapper
from player_results_wrapper import PlayerResultsWrapper
from supervillain_stack_wrapper import SuperVillainStackWrapper
from turn_wrapper import TurnWrapper

from Game.player_order_helper import GetPlayersStartingWith
from Game.Sources.source_types import KICK, LINE_UP
from Server.Game.Notifications.notification_wrapper_factory import NotificationWrapperFactory
from Server.Game.Requests.request_wrapper_factory import RequestWrapperFactory

class GameWrapper:
    """ A Wrapper for a Game that handles its conversion to and from JSON """
    
    def __init__(self, id, game, players):
        """ Initialize the Game Wrapper """
        self.id = id
        self.game = game
        self.players = players
        
    def canBuy(self, card):
        """ Return if the player can buy the given card """
        return self.game.currentTurn.power >= card.cost
        
    def toJSON(self, includeActions=False):
        """ Return the game as a JSON Dictionary """
        kicksJSON = GetCardListJSON(self.game.kickDeck, self.game, actions=[{'type':'BUY', 'source':KICK}], includeActions=includeActions, canBuyCallback=self.canBuy)
        weaknessesJSON = GetCardListJSON(self.game.weaknessDeck, self.game, includeActions=includeActions)
        destroyedJSON = GetCardListJSON(self.game.destroyedDeck, self.game, includeActions=includeActions)
        lineUpJSON = GetCardListJSON(self.game.lineUp.cards, self.game, actions=[{'type':'BUY', 'source':LINE_UP}], includeActions=includeActions, canBuyCallback=self.canBuy)
        
        gameJSON = {'id':self.id,
                    'isOver':self.game.isOver,
                    'mainDeck':{'count':len(self.game.mainDeck),
                                'hidden':True},
                    'superVillains':SuperVillainStackWrapper(self.game.superVillainStack).toJSON(includeActions=includeActions, canBuyCallback=self.canBuy),
                    'kicks':{'cards':kicksJSON, 'count':len(kicksJSON)},
                    'weaknesses':{'cards':weaknessesJSON, 'count':len(weaknessesJSON)},
                    'destroyed':{'cards':destroyedJSON, 'count':len(destroyedJSON), 'name':'Destroyed Deck'},
                    'lineUp':lineUpJSON,
                    'turn':TurnWrapper(self.game.currentTurn).toJSON(includeActions=includeActions)}
                    
        return {'game':gameJSON}
                
    def toJSONForPlayer(self, playerId):
        """ Return the more detailed JSON for the given player """
        request = self.game.currentTurn.request
        yourPlayer = self.players[playerId]
        
        isYourTurn = yourPlayer is self.game.currentTurn.player
        includeActions = isYourTurn and (request is None or yourPlayer in request.players)
                    
        requestWrapper = None
        if request is not None:
            requestWrapper = RequestWrapperFactory.buildRequestWrapper(self.game.currentTurn.request, self.game)
        
        json = self.toJSON(includeActions=includeActions)
        gameJSON = json['game']
        gameJSON['you'] = PlayerWrapper(yourPlayer, self.game, requestWrapper).toJSONForYourself(includeActions=includeActions)
        gameJSON['notifications'] = [NotificationWrapperFactory.buildWrapper(notification, self.game, yourPlayer).toJSON() for notification in self.game.notificationTracker.latestNotifications]
        gameJSON['players'] = [PlayerWrapper(player, self.game, requestWrapper).toJSON(includeActions=False) for player in GetPlayersStartingWith(yourPlayer, self.game.players) if player is not yourPlayer]
                    
        if requestWrapper is not None and yourPlayer in request.players:
            gameJSON['request'] = requestWrapper.toJSON(includeActions=True)
        return json
                
    def toResultJSONForPlayer(self, playerId):
        """ Return the more detailed JSON for the given player """
        json = {}
        json['players'] = [PlayerResultsWrapper(player, id == playerId).toJSON(self.game) for id, player in self.players.items()]
        return json