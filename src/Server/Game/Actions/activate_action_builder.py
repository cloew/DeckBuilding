from Server.urls import activateCardURL

class ActivateActionBuilder:
    """ Represents a builder that can construct valid Activate Card Actions """
    
    def __init__(self, zone, game):
        """ Return the Action JSON for the card given """
        self.game = game
        self.zone = zone
    
    def canBuildFor(self, card):
        """ Return if the builder can construct the action for the given card """
        if card in self.game.currentTurn.activatableEffects:
            activatableEffect = self.game.currentTurn.activatableEffects[card][0]
            if activatableEffect.canActivate(self.game):
                return True
        return False
    
    def buildFor(self, card, gameId, playerId):
        """ Return the Action JSON for the card given """
        return {'type':'ACTIVATE', 'zone':self.zone, 'apiUrl':activateCardURL.build(gameId=gameId, playerId=playerId, cardId=card.gameId)}