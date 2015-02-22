from request import Request

class PickCardRequest(Request):
    """ Represents a Request to Pick Cards """
    
    def __init__(self, cards, player, number, toDescription):
        """ Initialize the Request with the potential options """
        self.cards = list(cards)
        self.number = number
        self.toDescription = toDescription
        Request.__init__(self, [player])