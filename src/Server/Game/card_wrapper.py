
class CardWrapper:
    """ A Wrapper for a Card """
    
    def __init__(self, card):
        """ Initialize the Game Wrapper """
        self.card = card
        
    def toJSON(self):
        """ Return the game as a JSON Dictionary """
        return {'name':self.card.name,
                'cost':self.card.calculateCost()}