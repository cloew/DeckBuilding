from kao_json import JsonConfig, JsonAttr, FieldAttr

from request_config import RequestConfig

from Game.Commands.Requests.choose_option_request import ChooseOptionRequest
from Game.Commands.Requests.defend_request import DefendRequest
from Game.Commands.Requests.pick_card_request import PickCardRequest
from Game.Commands.Requests.pick_up_to_n_card_request import PickUpToNCardRequest
from Game.Commands.Requests.pick_up_to_n_cost_request import PickUpToNCostRequest

from Server.Game.Actions.pick_action_builder import PickActionBuilder
    
requestConfig = [RequestConfig(ChooseOptionRequest, [JsonAttr('options', lambda request: [option.description for option in request.options]),
                                                     FieldAttr('cards', field='relevantCards')
                                                     ]),
                 RequestConfig(DefendRequest, [FieldAttr('attack', field='attackCard'),
                                               FieldAttr('defenses', extraArgsProvider=lambda request, kwargs: {'actionBuilders':[PickActionBuilder()]})
                                               ]),
                 RequestConfig([PickCardRequest, PickUpToNCardRequest], [FieldAttr('cards', extraArgsProvider=lambda request, kwargs: {'actionBuilders':[PickActionBuilder()]}),
                                                                         FieldAttr('to', field='toDescription'),
                                                                         FieldAttr('number')]),
                 RequestConfig(PickUpToNCostRequest, [FieldAttr('cost')]).inheritFrom(PickCardRequest, ignore=['number'])
                 ]