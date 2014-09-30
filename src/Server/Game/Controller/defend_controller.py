from Game.Commands.Responses.defend import Defend
from Server.Game.games import games

from kao_flask.controllers.json_controller import JSONController

class DefendController(JSONController):
    """ Controller to defend """
    
    def performWithJSON(self, gameId, playerId):
        game = games[gameId]
        defending = self.json['defending']
        card = None
        if defending:
            cardIndex = self.json['index']
            card = game.game.currentTurn.request.defenses[cardIndex]
        
        Defend(card, game.game.currentTurn).perform()
        return game.toJSONForPlayer(playerId)