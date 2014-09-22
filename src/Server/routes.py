from Server.Game.Controller.get_game_controller import GetGameController
from Server.Game.Controller.activate_card_controller import ActivateCardController
from Server.Game.Controller.buy_card_controller import BuyCardController
from Server.Game.Controller.choose_controller import ChooseController
from Server.Game.Controller.end_turn_controller import EndTurnController
from Server.Game.Controller.pick_card_controller import PickCardController
from Server.Game.Controller.play_card_controller import PlayCardController

from Server.Lobby.Controller.change_character_controller import ChangeCharacterController
from Server.Lobby.Controller.get_lobbies_controller import GetLobbiesController
from Server.Lobby.Controller.get_lobby_controller import GetLobbyController
from Server.Lobby.Controller.get_lobby_for_player_controller import GetLobbyForPlayerController
from Server.Lobby.Controller.join_lobby_controller import JoinLobbyController
from Server.Lobby.Controller.new_lobby_controller import NewLobbyController
from Server.Lobby.Controller.start_game_controller import StartGameController

from kao_flask.endpoint import Endpoint
from kao_flask.controllers.html_controller import HTMLController

routes = [Endpoint('/', get=HTMLController('Server/templates/index.html')),
          #Game Endpoints
          Endpoint('/api/game/<int:gameId>', get=GetGameController()),
          Endpoint('/api/game/<int:gameId>/activate', post=ActivateCardController()),
          Endpoint('/api/game/<int:gameId>/buy', post=BuyCardController()),
          Endpoint('/api/game/<int:gameId>/choose', post=ChooseController()),
          Endpoint('/api/game/<int:gameId>/endturn', post=EndTurnController()),
          Endpoint('/api/game/<int:gameId>/pickcard', post=PickCardController()),
          Endpoint('/api/game/<int:gameId>/play', post=PlayCardController()),
          # Lobby Endpoints
          Endpoint('/api/lobbies', get=GetLobbiesController(), post=NewLobbyController()),
          Endpoint('/api/lobbies/<int:lobbyId>', get=GetLobbyController()),
          Endpoint('/api/lobbies/<int:lobbyId>/join', post=JoinLobbyController()),
          Endpoint('/api/lobbies/<int:lobbyId>/start', post=StartGameController()),
          Endpoint('/api/lobbies/<int:lobbyId>/player/<int:playerId>', get=GetLobbyForPlayerController()),
          Endpoint('/api/lobbies/<int:lobbyId>/player/<int:playerId>/changecharacter', post=ChangeCharacterController())]