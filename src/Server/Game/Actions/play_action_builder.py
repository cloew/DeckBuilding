from Server.urls import playCardURL

class PlayActionBuilder:
    """ Represents a builder that can construct valid Play Card Actions """
    
    def __init__(self, game, playerId):
        """ Return the Action JSON for the card given """
        self.game = game
        self.playerId = playerId
        
    def canBuildFor(self, card):
        """ Return if the builder can construct the action for the given card """
        return True
        
    def buildFor(self, card):
        """ Return the Action JSON for the card given """
        return {'type':'PLAY', 'apiUrl':playCardURL.build(gameId=self.game.id, playerId=self.playerId, cardId=card.gameId)}