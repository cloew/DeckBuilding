from card_wrapper import CardWrapper, GetCardListJSON
from player_wrapper import PlayerWrapper
from player_results_wrapper import PlayerResultsWrapper
from supervillain_stack_wrapper import SuperVillainStackWrapper
from turn_wrapper import TurnWrapper

from Game.player_order_helper import GetPlayersStartingWith
from Game.Zones.zone_types import KICK, LINE_UP

from Server.Game.Actions.buy_action_builder import BuyActionBuilder
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
        kicksJSON = GetCardListJSON(self.game.kickDeck, actionBuilders=[BuyActionBuilder(KICK, self.game)], includeActions=includeActions)
        weaknessesJSON = GetCardListJSON(self.game.weaknessDeck, includeActions=includeActions)
        destroyedJSON = GetCardListJSON(self.game.destroyedDeck, includeActions=includeActions)
        lineUpJSON = GetCardListJSON(self.game.lineUp.cards, actionBuilders=[BuyActionBuilder(LINE_UP, self.game)], includeActions=includeActions)
        
        gameJSON = {'id':self.id,
                    'isOver':self.game.isOver,
                    'mainDeck':{'count':len(self.game.mainDeck),
                                'hidden':True},
                    'superVillains':SuperVillainStackWrapper(self.game.superVillainStack, self.game).toJSON(includeActions=includeActions),
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
        includeActions = isYourTurn and request is None
                    
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
        yourPlayer = self.players[playerId]
        playersJSON = [PlayerResultsWrapper(playerResults, playerResults.player is yourPlayer).toJSON(self.game) for playerResults in self.game.results.playerResults]
        json['players'] = playersJSON
        return json