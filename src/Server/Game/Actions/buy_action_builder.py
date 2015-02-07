
class BuyActionBuilder:
    """ Represents a builder that can construct valid Buy Card Actions """
    
    def __init__(self, zone, game):
        """ Return the Action JSON for the card given """
        self.game = game
        self.zone = zone
    
    def canBuildFor(self, card):
        """ Return if the builder can construct the action for the given card """
        return self.game.currentTurn.power >= card.cost
    
    def buildFor(self, card):
        """ Return the Action JSON for the card given """
        return {'type':'BUY', 'zone':self.zone}