from Server.Game.card_wrapper import CardWrapper
from Server.Game.json_helper import GetCardListJSON

class DefendRequestWrapper:
    """ A Wrapper for a Defend Request that handles its conversion to JSON """
    PENDING_MESSAGE = "Picking a defense"
    
    def __init__(self, id, request, game):
        """ Initialize the Request Wrapper """
        self.id = id
        self.request = request
        self.game = game
        
    def toJSON(self, includeActions=False):
        """ Return the request as a JSON Dictionary """
        return {'type':'DEFEND',
                'id':self.id,
                'attack':CardWrapper(self.request.attackCard).toJSON(),
                'defenses':GetCardListJSON(self.request.defenses, self.game, actions=[{"type":"PICK"}], includeActions=True)}