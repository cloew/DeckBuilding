from request import Request
from Game.Sources.source_factory import SourceFactory

class ChooseOptionRequest(Request):
    """ Represents a Request to Choose an Option """
    
    def __init__(self, options, player, relevantCards=None):
        """ Initialize the Request with the potential options """
        self.options = options
        self.relevantCards = relevantCards
        Request.__init__(self, [player])