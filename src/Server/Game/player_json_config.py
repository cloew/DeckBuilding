from kao_json import JsonAttr, FieldAttr

from deck_json_config import GetVisibleDeckKwargs

from Game.player import Player
from Game.Commands.Requirements.current_player import CurrentPlayer
from Game.Zones.zone_types import CHARACTER, ONGOING

from Server.Game.Actions.activate_action_builder import ActivateActionBuilder
from Server.Game.Actions.play_action_builder import PlayActionBuilder

from kao_deck.deck import Deck
    
def GetHand(player, isYou):
    """ Return the player's hand """
    if isYou:
        return player.hand
    else:
        return Deck(items=player.hand)
        
def GetPlayerHandKwargs(player, kwargs):
    """ Return the Kwargs for the player's discard pile """
    if kwargs['isYou']:
        return {'actionBuilders':[PlayActionBuilder()]}
    else:
        return {'hidden':True, 'name':GetPlayerDeckHeader(player, kwargs) + " Hand"}
        
def GetPlayerDeckHeader(player, kwargs):
    """ Return the header for the player's name """
    if kwargs['isYou']:
        return "Your"
    else:
        return player.name + "'s"

playerConfig = [(Player, [FieldAttr('name'),
                          FieldAttr('character', extraArgsProvider=lambda turn, kwargs: {'actionBuilders':[ActivateActionBuilder(CHARACTER, kwargs['game'])]}),
                          FieldAttr('ongoing', extraArgsProvider=lambda turn, kwargs: {'actionBuilders':[ActivateActionBuilder(ONGOING, kwargs['game'])]}),
                          JsonAttr('isTurn', CurrentPlayer().passed, args=['game']),
                          FieldAttr('deck', extraArgsProvider=lambda player, kwargs: {'hidden':True, 'name':GetPlayerDeckHeader(player, kwargs) + " Deck"}),
                          FieldAttr('discardPile', field='deck.discardPile', extraArgsProvider=lambda player, kwargs: GetVisibleDeckKwargs(GetPlayerDeckHeader(player, kwargs) + " Discard Pile", includeActions=kwargs['includeActions'])),
                          JsonAttr('hand', GetHand, args=['isYou'], extraArgsProvider=GetPlayerHandKwargs)
                          ])]