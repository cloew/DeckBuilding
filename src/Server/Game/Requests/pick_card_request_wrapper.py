from Server.Game.json_helper import GetCardListJSON

class PickCardRequestWrapper:
    """ A Wrapper for a Pick Card Request that handles its conversion to JSON """
    PENDING_MESSAGE = "Picking cards"
    
    def __init__(self, id, request, game):
        """ Initialize the Request Wrapper """
        self.id = id
        self.request = request
        self.game = game
        
    def toJSON(self, includeActions=False):
        """ Return the request as a JSON Dictionary """
        return {'type':'PICK_CARD',
                'id':self.id,
                'cards':GetCardListJSON(self.request.cards, self.game, actions=[{"type":"PICK"}], includeActions=includeActions),
                'number':self.request.number}