
class PickUpToNCostRequest:
    """ Represents a Request to Pick Up to Some Cost of Cards """
    
    def __init__(self, cards, player, cost, toDescription):
        """ Initialize the Request with the potential options """
        self.cards = cards
        self.cost = cost
        self.toDescription = toDescription
        Request.__init__(self, [player])