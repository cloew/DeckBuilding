from source import Source

class EventSource(Source):
    """ Represents a potential source """
    
    def __init__(self, event):
        """ Initialize the source """
        sourceType = None
        self.event = event
        if hasattr(event, "fromSource") and event.fromSource is not None:
            sourceType = event.fromSource.sourceType
        elif hasattr(event, "sources") and event.sources is not None and len(event.sources) > 0:
            sourceType = event.sources[0].sourceType
        Source.__init__(self, event, sourceType=sourceType)
        
    @property
    def player(self):
        """ Return the current player """
        return self.event.player