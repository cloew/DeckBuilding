from Server.urls import buyCardURL

from Game.Commands.Requirements.enough_power import EnoughPower

class BuyActionBuilder:
    """ Represents a builder that can construct valid Buy Card Actions """
    
    def __init__(self, zone, game):
        """ Return the Action JSON for the card given """
        self.game = game
        self.zone = zone
    
    def canBuildFor(self, card):
        """ Return if the builder can construct the action for the given card """
        return EnoughPower(card).passed(None, self.game)
    
    def buildFor(self, card, gameId, playerId):
        """ Return the Action JSON for the card given """
        return {'type':'BUY', 'zone':self.zone.name, 'apiUrl':buyCardURL.build(gameId=gameId, playerId=playerId, cardId=card.gameId)}