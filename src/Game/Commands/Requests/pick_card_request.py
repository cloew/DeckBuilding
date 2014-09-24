from request import Request

class PickCardRequest(Request):
    """ Represents a Request to Pick Cards """
    
    def __init__(self, cards, player, number):
        """ Initialize the Request with the potential options """
        self.cards = cards
        self.number = number
        Request.__init__(self, [player])