from kao_json import JsonConfig, JsonAttr, KeywordAttr

from request_tracker import GetRequestIdFor

from Game.Commands.Requests.choose_option_request import ChooseOptionRequest
from Game.Commands.Requests.defend_request import DefendRequest
from Game.Commands.Requests.pick_card_request import PickCardRequest
from Game.Commands.Requests.pick_up_to_n_card_request import PickUpToNCardRequest
from Game.Commands.Requests.pick_up_to_n_cost_request import PickUpToNCostRequest

REQUEST_TO_TYPE = {ChooseOptionRequest:"CHOICE",
                   DefendRequest:"DEFEND",
                   PickCardRequest:"PICK_CARD",
                   PickUpToNCardRequest:"PICK_UP_TO_N_CARD",
                   PickUpToNCostRequest:"PICK_UP_TO_N_COST"}

REQUEST_TO_PENDING_TEXT = {ChooseOptionRequest:"{0} is choosing an option",
                           DefendRequest:"{0} is picking a defense",
                           PickCardRequest:"{0} is picking cards",
                           PickUpToNCardRequest:"{0} is picking cards",
                           PickUpToNCostRequest:"{0} is picking cards"}
    
def GetPendingActionText(request):
    """ Return the pending action text """
    pendingAction = None
    if request is not None:
        player = request.players[0]
        pendingAction = REQUEST_TO_PENDING_TEXT[request.__class__].format(player.name)
    return pendingAction
        
TypeAttr = JsonAttr('type', lambda request: REQUEST_TO_TYPE[request.__class__])
IdAttr = JsonAttr('id', GetRequestIdFor, args=['gameId'])
ForYouAttr = KeywordAttr('forYou')
PendingTextAttr = JsonAttr('pending', GetPendingActionText)

class RequestConfig(JsonConfig):
    """ Represents the Json Config for the Game Mode """
    
    def __init__(self, objectClass, attrs, optionalKwargs=None):
        """ Initialize the Game Mode Config """
        self.attrsIfForYou = attrs
        JsonConfig.__init__(self, objectClass, [TypeAttr, IdAttr, ForYouAttr, PendingTextAttr], optionalKwargs=optionalKwargs)
        
    def getAttrs(self, request, kwargs, classToConfig):
        """ Return the attributes for the Configuration """
        attrs = JsonConfig.getAttrs(self, request, kwargs, classToConfig)
        if kwargs['forYou']:
            attrs += self.attrsIfForYou
        return attrs