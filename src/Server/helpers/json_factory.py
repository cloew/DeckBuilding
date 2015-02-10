from kao_json import JsonFactory

from Server.Game.game_json_config import gameConfig
from Server.Lobby.lobby_json_config import lobbyConfig

jsonFactory = JsonFactory(gameConfig+lobbyConfig)