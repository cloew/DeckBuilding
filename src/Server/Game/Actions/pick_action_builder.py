
class PickActionBuilder:
    """ Represents a builder that can construct valid Pick Card Actions """
    
    def canBuildFor(self, card):
        """ Return if the builder can construct the action for the given card """
        return True
        
    def buildFor(self, card, gameId, playerId):
        """ Return the Action JSON for the card given """
        return {'type':'PICK'}