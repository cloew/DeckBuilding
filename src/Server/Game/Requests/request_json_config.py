from kao_json import JsonConfig, JsonAttr, FieldAttr

from request_config import RequestConfig

from Game.Commands.Requests.choose_option_request import ChooseOptionRequest
from Game.Commands.Requests.defend_request import DefendRequest
from Game.Commands.Requests.pick_card_request import PickCardRequest
from Game.Commands.Requests.pick_up_to_n_card_request import PickUpToNCardRequest
from Game.Commands.Requests.pick_up_to_n_cost_request import PickUpToNCostRequest

from Server.Game.Actions.pick_action_builder import PickActionBuilder
import Server.urls as urls
    
requestConfig = [RequestConfig(ChooseOptionRequest, [JsonAttr('options', lambda request: [option.description for option in request.options]),
                                                     FieldAttr('cards', field='relevantCards'),
                                                     JsonAttr('chooseUrl', lambda request, gameId, playerId: urls.chooseOptionURL.build(gameId=gameId, playerId=playerId), args=['gameId', 'playerId'])
                                                     ]),
                 RequestConfig(DefendRequest, [FieldAttr('attack', field='attackCard'),
                                               FieldAttr('defenses', extraArgsProvider=lambda request, kwargs: {'actionBuilders':[PickActionBuilder()]}),
                                               JsonAttr('defendUrl', lambda request, gameId, playerId: urls.defendURL.build(gameId=gameId, playerId=playerId), args=['gameId', 'playerId'])
                                               ]),
                 RequestConfig([PickCardRequest, PickUpToNCardRequest], [FieldAttr('cards', extraArgsProvider=lambda request, kwargs: {'actionBuilders':[PickActionBuilder()]}),
                                                                         FieldAttr('to', field='toDescription'),
                                                                         FieldAttr('number'),
                                                                         JsonAttr('pickUrl', lambda request, gameId, playerId: urls.pickCardURL.build(gameId=gameId, playerId=playerId), args=['gameId', 'playerId'])]),
                 RequestConfig(PickUpToNCostRequest, [FieldAttr('cost')]).inheritFrom(PickCardRequest, ignore=['number'])
                 ]