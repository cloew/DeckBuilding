from Game.Commands.Requests.choose_option_request import ChooseOptionRequest
from Game.Commands.Requests.defend_request import DefendRequest
from Game.Commands.Requests.pick_card_request import PickCardRequest
from Game.Commands.Requests.pick_up_to_n_card_request import PickUpToNCardRequest

from Server.Game.Requests.choose_option_request_wrapper import ChooseOptionRequestWrapper
from Server.Game.Requests.defend_request_wrapper import DefendRequestWrapper
from Server.Game.Requests.pick_card_request_wrapper import PickCardRequestWrapper
from Server.Game.Requests.pick_up_to_n_card_request_wrapper import PickUpToNCardRequestWrapper

class RequestWrapperFactory:
    """ Factory to construct Request Wrappers """
    REQUEST_TO_WRAPPER = {ChooseOptionRequest:ChooseOptionRequestWrapper,
                          DefendRequest:DefendRequestWrapper,
                          PickCardRequest:PickCardRequestWrapper,
                          PickUpToNCardRequest:PickUpToNCardRequestWrapper}
    
    def buildRequestWrapper(self, request, game):
        """ Return the current Request Wrapper """
        if request.__class__ in self.REQUEST_TO_WRAPPER:
            return self.REQUEST_TO_WRAPPER[request.__class__](request, game)
            
RequestWrapperFactory = RequestWrapperFactory()