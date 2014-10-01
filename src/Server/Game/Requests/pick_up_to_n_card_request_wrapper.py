from Server.Game.json_helper import GetCardListJSON
from Server.Game.Requests.pick_card_request_wrapper import PickCardRequestWrapper

class PickUpToNCardRequestWrapper(PickCardRequestWrapper):
    """ A Wrapper for a Pick Up To N Card Request that handles its conversion to JSON """
        
    def toJSON(self, includeActions=False):
        """ Return the request as a JSON Dictionary """
        json = PickCardRequestWrapper.toJSON(includeActions=includeActions)
        json['type'] = 'PICK_UP_TO_N_CARD'
        return json