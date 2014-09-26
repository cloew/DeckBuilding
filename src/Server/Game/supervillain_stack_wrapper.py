from card_wrapper import CardWrapper
from Game.Sources.source_factory import SUPERVILLAIN

class SuperVillainStackWrapper:
    """ A Wrapper for the Super Villain Stack that handles its conversion to JSON """
    
    def __init__(self, superVillainStack):
        """ Initialize the Game Wrapper """
        self.superVillainStack = superVillainStack
        
    def toJSON(self, includeActions=False):
        """ Return the supervillain stack as a JSON Dictionary """
        superVillainJSON = {'count':len(self.superVillainStack), 'hidden':not self.superVillainStack.canPurchase}
        if self.superVillainStack.canPurchase and includeActions:
            superVillainJSON['cards'] = [CardWrapper(self.superVillainStack.topCard, actions=[{'type':'BUY', 'source':SUPERVILLAIN}]).toJSON()]
        
        return superVillainJSON