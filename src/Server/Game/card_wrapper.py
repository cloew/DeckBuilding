
class CardWrapper:
    """ A Wrapper for a Card """
    IMAGES_DIRECTORY_URL = 'static/images/Cards/'
    
    def __init__(self, card):
        """ Initialize the Card Wrapper """
        self.card = card
        
    def toJSON(self, actionBuilders=[], includeActions=False):
        """ Return the card as a JSON Dictionary """
        actions = []
        if includeActions:
            actions = [actionBuilder.buildFor(self.card) for actionBuilder in actionBuilders if actionBuilder.canBuildFor(self.card)]
        return {'name':self.card.name,
                'cost':self.card.calculateCost(),
                'actions':actions,
                'imageUrl':self.IMAGES_DIRECTORY_URL+self.card.image}
                
def GetCardListJSON(cards, actionBuilders=[], includeActions=False):
    """ Return a list of Card JSON """
    return [CardWrapper(card).toJSON(actionBuilders=actionBuilders, includeActions=includeActions) for card in cards]