import Server.urls as urls

from Server.Game.Controller.get_game_for_player_controller import GetGameForPlayerController
from Server.Game.Controller.activate_card_controller import ActivateCardController
from Server.Game.Controller.buy_card_controller import BuyCardController
from Server.Game.Controller.choose_controller import ChooseController
from Server.Game.Controller.defend_controller import DefendController
from Server.Game.Controller.end_turn_controller import EndTurnController
from Server.Game.Controller.pick_card_controller import PickCardController
from Server.Game.Controller.play_card_controller import PlayCardController
from Server.Game.Controller.get_results_for_player_controller import GetResultsForPlayerController

from Server.Lobby.Controller.change_character_controller import ChangeCharacterController
from Server.Lobby.Controller.change_deck_for_role_controller import ChangeDeckForRoleController
from Server.Lobby.Controller.change_number_of_villains_controller import ChangeNumberOfVillainsController
from Server.Lobby.Controller.change_name_controller import ChangeNameController
from Server.Lobby.Controller.get_characters_controller import GetCharactersController
from Server.Lobby.Controller.get_lobbies_controller import GetLobbiesController
from Server.Lobby.Controller.get_lobby_for_player_controller import GetLobbyForPlayerController
from Server.Lobby.Controller.join_lobby_controller import JoinLobbyController
from Server.Lobby.Controller.new_lobby_controller import NewLobbyController
from Server.Lobby.Controller.start_game_controller import StartGameController

from kao_flask.endpoint import Endpoint
from kao_flask.controllers.html_controller import HTMLController

routes = [Endpoint('/', get=HTMLController('Server/templates/index.html')),
          #Game Endpoints
          Endpoint('/api/game/<int:gameId>/player/<int:playerId>', get=GetGameForPlayerController()),
          Endpoint('/api/game/<int:gameId>/player/<int:playerId>/results', get=GetResultsForPlayerController()),
          Endpoint(urls.endTurnURL, post=EndTurnController()),
          Endpoint('/api/game/<int:gameId>/player/<int:playerId>/choose', post=ChooseController()),
          Endpoint('/api/game/<int:gameId>/player/<int:playerId>/defend', post=DefendController()),
          Endpoint('/api/game/<int:gameId>/player/<int:playerId>/pickcard', post=PickCardController()),
          Endpoint(urls.activateCardURL, post=ActivateCardController()),
          Endpoint(urls.buyCardURL, post=BuyCardController()),
          Endpoint(urls.playCardURL, post=PlayCardController()),
          # Lobby Endpoints
          Endpoint('/api/lobbies', get=GetLobbiesController(), post=NewLobbyController()),
          Endpoint('/api/lobbies/<int:lobbyId>/player/<int:playerId>', get=GetLobbyForPlayerController()),
          Endpoint(urls.joinLobbyURL, post=JoinLobbyController()),
          Endpoint(urls.startGameURL, post=StartGameController()),
          Endpoint(urls.changeCharacterURL, post=ChangeCharacterController()),
          Endpoint(urls.changeNameURL, post=ChangeNameController()),
          Endpoint(urls.changeDeckURL, post=ChangeDeckForRoleController()),
          Endpoint(urls.changeNumberOfVillainsURL, post=ChangeNumberOfVillainsController()),
          # Character Endpoints
          Endpoint('/api/characters', get=GetCharactersController()),]