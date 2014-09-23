from request import Request
from Game.Sources.source_factory import SourceFactory

class ChooseOptionRequest(Request):
    """ Represents a Request to Choose an Option """
    
    def __init__(self, options, args, relevantSourceType=None):
        """ Initialize the Request with the potential options """
        self.options = options
        self.args = args
        self.relevantSourceType = relevantSourceType
        Request.__init__(self, [args.player])
        
    @property
    def relevantSource(self):
        """ Return the relevant source if any """
        if self.relevantSourceType is not None:
            return SourceFactory.getSourceForEffect(self.relevantSourceType, self.args)
        else:
            return None