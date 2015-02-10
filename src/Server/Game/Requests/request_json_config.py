from kao_json import JsonConfig, JsonAttr, FieldAttr

from request_tracker import GetRequestIdFor

from Game.Commands.Requests.choose_option_request import ChooseOptionRequest
from Game.Commands.Requests.defend_request import DefendRequest
from Game.Commands.Requests.pick_card_request import PickCardRequest
from Game.Commands.Requests.pick_up_to_n_card_request import PickUpToNCardRequest
from Game.Commands.Requests.pick_up_to_n_cost_request import PickUpToNCostRequest

from Game.Commands.Requirements.request_target import RequestTarget

from Server.Game.Actions.pick_action_builder import PickActionBuilder

REQUEST_TO_TYPE = {ChooseOptionRequest:"CHOICE",
                   DefendRequest:"DEFEND",
                   PickCardRequest:"PICK_CARD",
                   PickUpToNCardRequest:"PICK_UP_TO_N_CARD",
                   PickUpToNCostRequest:"PICK_UP_TO_N_COST"}

REQUEST_TO_PENDING_TEXT = {ChooseOptionRequest:"Making a choice",
                           DefendRequest:"Picking a defense",
                           PickCardRequest:"Picking cards",
                           PickUpToNCardRequest:"Picking cards",
                           PickUpToNCostRequest:"Picking cards"}
        
TypeAttr = JsonAttr('type', lambda request: REQUEST_TO_TYPE[request.__class__])
IdAttr = JsonAttr('id', GetRequestIdFor, args=['gameId'])
        
def GetPlayerPendingAction(player, game):
    """ Return the pending action """
    pendingAction = None
    if RequestTarget().passed(player, game):
        pendingAction = REQUEST_TO_PENDING_TEXT[game.currentTurn.request.__class__]
    return pendingAction
    
requestConfig = [(ChooseOptionRequest, [TypeAttr,
                                        IdAttr,
                                        JsonAttr('options', lambda request: [option.description for option in request.options]),
                                        FieldAttr('cards', field='relevantCards')
                                        ]),
                 (DefendRequest, [TypeAttr,
                                  IdAttr,
                                  FieldAttr('attack', field='attackCard'),
                                  FieldAttr('defenses', extraArgsProvider=lambda request, kwargs: {'actionBuilders':[PickActionBuilder()]})
                                  ]),
                 ([PickCardRequest, PickUpToNCardRequest], [TypeAttr,
                                                            IdAttr,
                                                            FieldAttr('cards', extraArgsProvider=lambda request, kwargs: {'actionBuilders':[PickActionBuilder()]}),
                                                            FieldAttr('to', field='toDescription'),
                                                            FieldAttr('number')]),
                 JsonConfig(PickUpToNCostRequest, [FieldAttr('cost')]).inheritFrom(PickCardRequest, ignore=['number'])
                 ]