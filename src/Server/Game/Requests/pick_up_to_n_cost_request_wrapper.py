from Server.Game.Requests.pick_card_request_wrapper import PickCardRequestWrapper

class PickUpToNCostRequestWrapper(PickCardRequestWrapper):
    """ A Wrapper for a Pick Up To N Cost Request that handles its conversion to JSON """
        
    def toJSON(self, includeActions=False):
        """ Return the request as a JSON Dictionary """
        json = PickCardRequestWrapper.toCoreJSON(self, includeActions=includeActions)
        json['type'] = 'PICK_UP_TO_N_COST'
        json['cost'] = self.request.cost
        return json