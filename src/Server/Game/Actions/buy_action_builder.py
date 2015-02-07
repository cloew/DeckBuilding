from Server.urls import buyCardURL

from Game.Commands.Requirements.enough_power import EnoughPower

class BuyActionBuilder:
    """ Represents a builder that can construct valid Buy Card Actions """
    
    def __init__(self, zone, game, playerId):
        """ Return the Action JSON for the card given """
        self.game = game
        self.zone = zone
        self.playerId = playerId
    
    def canBuildFor(self, card):
        """ Return if the builder can construct the action for the given card """
        return EnoughPower(card).passed(None, self.game.game)
    
    def buildFor(self, card):
        """ Return the Action JSON for the card given """
        return {'type':'BUY', 'zone':self.zone, 'apiUrl':buyCardURL.build(gameId=self.game.id, playerId=self.playerId, cardId=card.gameId)}