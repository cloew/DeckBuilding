from Server.Game.card_wrapper import CardWrapper
from Server.Game.json_helper import GetCardListJSON

class DefendRequestWrapper:
    """ A Wrapper for a Defend Request that handles its conversion to JSON """
    
    def __init__(self, request, game):
        """ Initialize the Request Wrapper """
        self.request = request
        self.game = game
        
    def toJSON(self, includeActions=False):
        """ Return the request as a JSON Dictionary """
        return {'type':'DEFEND',
                'attack':CardWrapper(self.request.attackCard).toJSON(),
                'defenses':GetCardListJSON(self.request.defenses, self.game, actions=[{"type":"PICK"}], includeActions=True)}