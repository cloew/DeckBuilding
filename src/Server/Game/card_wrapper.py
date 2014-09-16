
class CardWrapper:
    """ A Wrapper for a Card """
    IMAGES_DIRECTORY_URL = 'static/images/'
    
    def __init__(self, card, actions=[]):
        """ Initialize the Card Wrapper """
        self.card = card
        self.actions = actions
        
    def toJSON(self):
        """ Return the card as a JSON Dictionary """
        return {'name':self.card.name,
                'cost':self.card.calculateCost(),
                'actions':self.actions,
                'imageUrl':self.IMAGES_DIRECTORY_URL+self.card.image}