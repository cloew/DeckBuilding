from Game.Commands.Requests.choose_option_request import ChooseOptionRequest

from Server.Game.Requests.choose_option_request_wrapper import ChooseOptionRequestWrapper

class RequestWrapperFactory:
    """ Factory to construct Request Wrappers """
    REQUEST_TO_WRAPPER = {ChooseOptionRequest:ChooseOptionRequestWrapper}
    
    def buildRequestWrapper(self, request):
        """ Return the current Request Wrapper """
        if request.__class__ in self.REQUEST_TO_WRAPPER:
            return self.REQUEST_TO_WRAPPER[request.__class__](request)
            
RequestWrapperFactory = RequestWrapperFactory()