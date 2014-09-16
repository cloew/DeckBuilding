from Game.Sources.source_factory import SourceFactory

class ChooseOptionRequest:
    """ Represents a Request to Choose an Option """
    
    def __init__(self, options, args, relevantSourceType=None):
        """ Initialize the Request with the potential options """
        self.options = options
        self.args = args
        self.relevantSourceType = relevantSourceType
        
    @property
    def relevantSource(self):
        """ Return the relevant source if any """
        if self.relevantSourceType is not None:
            return SourceFactory.getSource(self.relevantSourceType, self.args.game, event=self.args.event)
        else:
            return None