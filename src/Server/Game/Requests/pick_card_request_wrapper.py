from Server.Game.json_helper import GetCardListJSON

class PickCardRequestWrapper:
    """ A Wrapper for a Pick Card Request that handles its conversion to JSON """
    
    def __init__(self, request):
        """ Initialize the Request Wrapper """
        self.request = request
        
    def toJSON(self):
        """ Return the request as a JSON Dictionary """
        return {'type':'PICK_CARD',
                'cards':GetCardListJSON(self.request.cards)}