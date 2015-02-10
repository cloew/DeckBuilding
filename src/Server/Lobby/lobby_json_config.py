from kao_json import JsonConfig, JsonAttr, FieldAttr, KeywordAttr

from game_mode_config import GameModeConfig

from Lobby.lobby import Lobby
from Lobby.player_in_lobby import PlayerInLobby
from Lobby.Settings.deck_setting import DeckSetting

lobbyConfig = [JsonConfig(Lobby, [FieldAttr('id'),
                                  FieldAttr('gamemode'),
                                  KeywordAttr('you', keyword='currentPlayer'),
                                  JsonAttr('players', lambda lobby, playerId: [player for player in lobby.players if player.id != playerId], args=['playerId'])],
                                 optionalKwargs={'playerId':None, 'currentPlayer':None}),
               GameModeConfig(),
               (PlayerInLobby, [FieldAttr('id'),
                                FieldAttr('name'),
                                FieldAttr('character'),
                                FieldAttr('starting', field='startingDeckSetting')]),
               (DeckSetting, [FieldAttr('options', field='potentialDeckIds'),
                              FieldAttr('current', field='index')])
               ]