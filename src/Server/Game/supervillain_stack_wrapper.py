from card_wrapper import CardWrapper
from Game.Zones.zone_types import SUPERVILLAIN
from Server.Game.Actions.buy_action_builder import BuyActionBuilder

class SuperVillainStackWrapper:
    """ A Wrapper for the Super Villain Stack that handles its conversion to JSON """
    
    def __init__(self, superVillainStack, game):
        """ Initialize the Game Wrapper """
        self.superVillainStack = superVillainStack
        self.game = game
        
    def toJSON(self, includeActions=False):
        """ Return the supervillain stack as a JSON Dictionary """
        superVillainJSON = {'count':len(self.superVillainStack), 'hidden':not self.superVillainStack.available}
        self.addTopCard(superVillainJSON, includeActions=includeActions)
        return superVillainJSON
        
    def addTopCard(self, superVillainJSON, includeActions=False):
        """ Add the top card of the super villain stack if it's available """
        if self.superVillainStack.available:
            superVillainJSON['cards'] = [CardWrapper(self.superVillainStack.topCard).toJSON(actionBuilders=[BuyActionBuilder(SUPERVILLAIN, self.game)], includeActions=includeActions)]