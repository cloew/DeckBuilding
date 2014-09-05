
class CardWrapper:
    """ A Wrapper for a Card """
    
    def __init__(self, card):
        """ Initialize the Card Wrapper """
        self.card = card
        
    def toJSON(self):
        """ Return the card as a JSON Dictionary """
        return {'name':self.card.name,
                'cost':self.card.calculateCost()}