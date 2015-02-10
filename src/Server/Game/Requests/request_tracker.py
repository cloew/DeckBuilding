from helpers.incrementer import Incrementer

class RequestTracker:
    """ Represents a module that tracks requests by the game to give them uniqe ids """
    
    def __init__(self):
        """ Initialize the Request Tracker """
        self.id = 0
        self.idProvider = Incrementer(startAt=1)
        self.request = None
        
    def getIdFor(self, request):
        """ Return the current Request Wrapper """
        if request is not self.request:
            self.id = self.idProvider.next()
            self.request = request
        
        return self.id
        
gameIdToTracker = {}

def GetRequestIdFor(request, gameId):
    """ Return the Request Id for the provided game """
    global gameIdToTracker
    if gameId not in gameIdToTracker:
        gameIdToTracker[gameId] = RequestTracker()
    return gameIdToTracker[gameId].getIdFor(request)