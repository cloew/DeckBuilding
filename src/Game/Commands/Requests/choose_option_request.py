from request import Request

class ChooseOptionRequest(Request):
    """ Represents a Request to Choose an Option """
    
    def __init__(self, options, player, relevantCards=None):
        """ Initialize the Request with the potential options """
        self.options = options
        self.relevantCards = relevantCards
        Request.__init__(self, [player])