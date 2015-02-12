from kao_json import JsonConfig, JsonAttr, FieldAttr, KeywordAttr

from game_mode_config import GameModeConfig

from Lobby.lobby import Lobby
from Lobby.player_in_lobby import PlayerInLobby
from Lobby.Settings.deck_setting import DeckSetting

import Server.urls as urls

lobbyConfig = [JsonConfig(Lobby, [FieldAttr('id'),
                                  FieldAttr('gamemode', field='gameMode'),
                                  KeywordAttr('you', keyword='currentPlayer'),
                                  JsonAttr('players', lambda lobby, playerId: [player for player in lobby.players if player.id != playerId], args=['playerId']),
                                  JsonAttr('joinUrl', lambda lobby: urls.joinLobbyURL.build(lobbyId=lobby.id)),
                                  JsonAttr('startGameUrl', lambda lobby: urls.startGameURL.build(lobbyId=lobby.id)),
                                  JsonAttr('changeCharacterUrl', lambda lobby, playerId: urls.changeCharacterURL.build(lobbyId=lobby.id, playerId=playerId), args=['playerId']),
                                  JsonAttr('changeNameUrl', lambda lobby, playerId: urls.changeNameURL.build(lobbyId=lobby.id, playerId=playerId), args=['playerId']),
                                  JsonAttr('changeDeckUrl', lambda lobby, playerId: urls.changeDeckURL.build(lobbyId=lobby.id, playerId=playerId), args=['playerId']),
                                  JsonAttr('changeNumberOfVillainsUrl', lambda lobby, playerId: urls.changeNumberOfVillainsURL.build(lobbyId=lobby.id, playerId=playerId), args=['playerId'])],
                                 optionalKwargs={'playerId':None, 'currentPlayer':None}),
               GameModeConfig(),
               (PlayerInLobby, [FieldAttr('id'),
                                FieldAttr('name'),
                                FieldAttr('character'),
                                FieldAttr('starting', field='startingDeckSetting')]),
               (DeckSetting, [FieldAttr('options', field='potentialDeckIds'),
                              FieldAttr('current', field='index')])
               ]