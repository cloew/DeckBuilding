
class CardWrapper:
    """ A Wrapper for a Card """
    IMAGES_DIRECTORY_URL = 'static/images/'
    
    def __init__(self, card, canBuy=False, source=None):
        """ Initialize the Card Wrapper """
        self.card = card
        self.canBuy = canBuy
        self.source = source
        
    def toJSON(self):
        """ Return the card as a JSON Dictionary """
        return {'name':self.card.name,
                'cost':self.card.calculateCost(),
                'canBuy':self.canBuy,
                'source':self.source,
                'imageUrl':self.IMAGES_DIRECTORY_URL+self.card.image}