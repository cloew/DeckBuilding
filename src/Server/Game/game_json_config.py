from kao_json import JsonConfig, JsonAttr, FieldAttr, KeywordAttr

from deck_json_config import deckConfig, GetVisibleDeckKwargs
from player_json_config import playerConfig
from Server.Game.Notifications.notification_json_config import notificationConfig
from Server.Game.Requests.request_json_config import requestConfig
from Server.Game.Results.game_results_json_config import resultsConfig

from Game.game import Game
from Game.player_order_helper import GetPlayersStartingWith
from Game.supervillain_stack import SuperVillainStack
from Game.turn import Turn
from Game.Card.card import Card
from Game.Characters.character import Character

from Game.Commands.Requirements.current_player import CurrentPlayer
from Game.Commands.Requirements.no_request import NoRequest
from Game.Commands.Requirements.request_target import RequestTarget

from Game.Zones.zone_types import KICK, LINE_UP, PLAYED, SUPERVILLAIN

from Server.Game.Actions.action_json_config import CardActionAttr
from Server.Game.Actions.activate_action_builder import ActivateActionBuilder
from Server.Game.Actions.buy_action_builder import BuyActionBuilder

import Server.urls as urls

CARD_IMAGES_DIRECTORY_URL = 'static/images/Cards/'
CHARACTER_IMAGES_DIRECTORY_URL = 'static/images/Characters/'

class PlayedWrapper:
    def __init__(self, turn):
        self.playedCards = turn.playedCards
        self.turn = turn
        
    @property
    def activatableIndices(self):
        return [self.playedCards.index(card) for card in self.playedCards if card in self.turn.activatableEffects]

def GetSuperVillainTopCard(stack):
    """ Returns if the quiz is for words """
    cards = []
    if stack.available:
        cards = [stack.topCard]
    return cards

def IncludeStandardActions(game, player):
    """ Return if actions should be included """
    return CurrentPlayer().passed(player, game) and NoRequest().passed(player, game)

def GetEndTurnUrl(turn, gameId, playerId, includeActions):
    """ Return if actions should be included """
    if includeActions:
        return urls.endTurnURL.build(gameId=gameId, playerId=playerId)
    else:
        return None

gameConfig = [(Game, [JsonAttr('id', lambda game, gameId: gameId, args=['gameId']),
                      FieldAttr('isOver'),
                      FieldAttr('mainDeck', extraArgsProvider=lambda game, kwargs: {'hidden':True, 'name':'Main Deck'}),
                      FieldAttr('superVillains', field='superVillainStack', extraArgsProvider=lambda game, kwargs: {'actionBuilders':[BuyActionBuilder(SUPERVILLAIN, game)], 'includeActions':IncludeStandardActions(game, kwargs['currentPlayer'])}),
                      FieldAttr('kicks', field='kickDeck', extraArgsProvider=lambda game, kwargs: GetVisibleDeckKwargs('Kick Deck', includeActions=IncludeStandardActions(game, kwargs['currentPlayer']), actionBuilders=[BuyActionBuilder(KICK, game)])),
                      FieldAttr('weaknesses', field='weaknessDeck', extraArgsProvider=lambda game, kwargs: GetVisibleDeckKwargs('Weakness Deck')),
                      FieldAttr('destroyed', field='destroyedDeck', extraArgsProvider=lambda game, kwargs: GetVisibleDeckKwargs('Destroyed Deck')),
                      JsonAttr('lineUp', lambda game: game.lineUp.cards, extraArgsProvider=lambda game, kwargs: {'actionBuilders':[BuyActionBuilder(LINE_UP, game)], 'includeActions':IncludeStandardActions(game, kwargs['currentPlayer'])}),
                      FieldAttr('turn', field='currentTurn', extraArgsProvider=lambda game, kwargs: {'includeActions':IncludeStandardActions(game, kwargs['currentPlayer'])}),
                      KeywordAttr('you', keyword='currentPlayer', extraArgsProvider=lambda game, kwargs: {'game':game, 'isYou':True, 'includeActions':IncludeStandardActions(game, kwargs['currentPlayer'])}),
                      JsonAttr('players', lambda game, currentPlayer: [player for player in GetPlayersStartingWith(currentPlayer, game.players) if player is not currentPlayer], args=['currentPlayer'], extraArgsProvider=lambda game, kwargs: {'game':game, 'isYou':False, 'includeActions':IncludeStandardActions(game, kwargs['currentPlayer'])}),
                      FieldAttr('notifications', field='notificationTracker.latestNotifications', extraArgsProvider=lambda game, kwargs: {'game':game})
                      ]),
              (Turn, [FieldAttr('power'),
                      FieldAttr('modifier'),
                      FieldAttr('playerName', field='player.name'),
                      KeywordAttr('canEndTurn', keyword='includeActions'),
                      FieldAttr('request', extraArgsProvider=lambda turn, kwargs: {'includeActions':True, 'forYou':RequestTarget().passed(kwargs['currentPlayer'], turn.game)}),
                      JsonAttr('played', PlayedWrapper, extraArgsProvider=lambda turn, kwargs: {'actionBuilders':[ActivateActionBuilder(PLAYED, turn.game)]}),
                      JsonAttr('endTurnUrl', GetEndTurnUrl, args=['gameId', 'playerId', 'includeActions'])
                      ]),
              (PlayedWrapper, [FieldAttr('cards', field='playedCards'),
                               FieldAttr('activatableIndices')
                               ]),
              (SuperVillainStack, [JsonAttr('count', lambda stack: len(stack)),
                                   JsonAttr('hidden', lambda stack: not stack.available),
                                   JsonAttr('cards', GetSuperVillainTopCard)
                                   ]),
              JsonConfig(Character, [FieldAttr('name'),
                                     FieldAttr('active'),
                                     CardActionAttr,
                                     JsonAttr('imageUrl', lambda character: CHARACTER_IMAGES_DIRECTORY_URL+character.image)],
                                    optionalKwargs={'includeActions':False, 'actionBuilders':[], 'gameId': None, 'playerId': None}),
              JsonConfig(Card, [FieldAttr('name'),
                                JsonAttr('cost', lambda card: card.calculateCost()),
                                CardActionAttr,
                                JsonAttr('imageUrl', lambda card: CARD_IMAGES_DIRECTORY_URL+card.image)],
                               optionalKwargs={'includeActions':False, 'actionBuilders':[], 'gameId': None, 'playerId': None})
             ] + deckConfig + playerConfig + requestConfig + notificationConfig + resultsConfig