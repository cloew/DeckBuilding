from card_wrapper import CardWrapper, GetCardListJSON
from game_character_wrapper import GameCharacterWrapper

from Server.Game.Actions.activate_action_builder import ActivateActionBuilder
from Server.Game.Actions.play_action_builder import PlayActionBuilder

from Game.Zones.zone_types import ONGOING, PLAYED

class PlayerWrapper:
    """ A Wrapper for a Game Player """
    
    def __init__(self, player, game, requestWrapper):
        """ Initialize the Player Wrapper """
        self.player = player
        self.game = game
        self.requestWrapper = requestWrapper
        
    def toJSON(self, includeActions=False):
        """ Return the Player as a JSON Dictionary """
        handJSON = GetCardListJSON(self.player.hand, actionBuilders=[PlayActionBuilder()], includeActions=includeActions)
        ongoingJSON = GetCardListJSON(self.player.ongoing, actionBuilders=[ActivateActionBuilder(ONGOING, self.game)], includeActions=includeActions)
        discardPileJSON = GetCardListJSON(self.player.deck.discardPile, includeActions=includeActions)
        characterJSON = GameCharacterWrapper(self.player.character, self.game).toJSON(includeActions=includeActions)
        
        return {'ongoing':ongoingJSON,
                'name':self.player.name,
                'character':characterJSON,
                'pending':self.getPendingAction(),
                'isTurn':self.player is self.game.currentTurn.player,
                'deck':{'count':len(self.player.deck),
                        'hidden':True},
                'discardPile':{'cards':discardPileJSON, 'count':len(discardPileJSON), 'name':self.player.name + "'s Discard Pile"},
                'hand':{'count':len(self.player.hand),
                        'hidden':True}}
                
    def toJSONForYourself(self, includeActions=False):
        """ Return the Player as a JSON Dictionary as if you are this player """
        handJSON = GetCardListJSON(self.player.hand, actionBuilders=[PlayActionBuilder()], includeActions=includeActions)
        json = self.toJSON(includeActions=includeActions)
        json['hand'] = handJSON
        json['discardPile']['name'] = "Your Discard Pile"
        
        return json
        
    def getPendingAction(self):
        """ Return the pending action """
        pendingAction = None
        if self.requestWrapper is not None and self.player in self.requestWrapper.request.players:
            pendingAction = self.requestWrapper.PENDING_MESSAGE
        return pendingAction