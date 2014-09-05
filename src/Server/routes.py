from Server.Controller.start_game_controller import StartGameController
from Server.Controller.get_game_controller import GetGameController

from kao_flask.endpoint import Endpoint
from kao_flask.controllers.html_controller import HTMLController

routes = [Endpoint('/', get=HTMLController('Server/templates/index.html')),
          Endpoint('/api/startgame', post=StartGameController()),
          Endpoint('/api/game/<int:gameId>', get=GetGameController())]