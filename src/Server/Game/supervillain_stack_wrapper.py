from card_wrapper import CardWrapper
from Game.Sources.source_types import SUPERVILLAIN

class SuperVillainStackWrapper:
    """ A Wrapper for the Super Villain Stack that handles its conversion to JSON """
    
    def __init__(self, superVillainStack):
        """ Initialize the Game Wrapper """
        self.superVillainStack = superVillainStack
        
    def toJSON(self, includeActions=False, canBuyCallback=None):
        """ Return the supervillain stack as a JSON Dictionary """
        superVillainJSON = {'count':len(self.superVillainStack), 'hidden':not self.superVillainStack.available}
        self.addTopCard(superVillainJSON, includeActions=includeActions, canBuyCallback=canBuyCallback)
        return superVillainJSON
        
    def addTopCard(self, superVillainJSON, includeActions=False, canBuyCallback=None):
        """ Add the top card of the super villain stack if it's available """
        if self.superVillainStack.available:
            if includeActions and canBuyCallback(self.superVillainStack.topCard):
                actions=[{'type':'BUY', 'source':SUPERVILLAIN}]
            else:
                actions=[]
            superVillainJSON['cards'] = [CardWrapper(self.superVillainStack.topCard, actions=actions).toJSON()]