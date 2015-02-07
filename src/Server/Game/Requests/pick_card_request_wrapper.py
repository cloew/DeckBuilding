from Server.Game.card_wrapper import GetCardListJSON
from Server.Game.Actions.pick_action_builder import PickActionBuilder

class PickCardRequestWrapper:
    """ A Wrapper for a Pick Card Request that handles its conversion to JSON """
    PENDING_MESSAGE = "Picking cards"
    
    def __init__(self, id, request, game):
        """ Initialize the Request Wrapper """
        self.id = id
        self.request = request
        self.game = game
        
    def toCoreJSON(self, includeActions=False):
        """ Return the request as a JSON Dictionary """
        return {'type':'PICK_CARD',
                'id':self.id,
                'cards':GetCardListJSON(self.request.cards, actionBuilders=[PickActionBuilder()], includeActions=includeActions),
                'to':self.request.toDescription}
        
    def toJSON(self, includeActions=False):
        """ Return the request as a JSON Dictionary """
        json = self.toCoreJSON(includeActions=includeActions)
        json['number'] = self.request.number
        return json