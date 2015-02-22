from request import Request

class PickUpToNCostRequest(Request):
    """ Represents a Request to Pick Up to Some Cost of Cards """
    
    def __init__(self, cards, player, cost, toDescription):
        """ Initialize the Request with the potential options """
        self.cards = list(cards)
        self.cost = cost
        self.toDescription = toDescription
        Request.__init__(self, [player])