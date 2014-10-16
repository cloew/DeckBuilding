from card_wrapper import CardWrapper
from game_character_wrapper import GameCharacterWrapper
from json_helper import GetCardListJSON

from Game.Sources.source_types import ONGOING, PLAYED

class PlayerWrapper:
    """ A Wrapper for a Game Player """
    
    def __init__(self, player, game, requestWrapper):
        """ Initialize the Player Wrapper """
        self.player = player
        self.game = game
        self.requestWrapper = requestWrapper
        
    def toJSON(self, includeActions=False):
        """ Return the Player as a JSON Dictionary """
        handJSON = GetCardListJSON(self.player.hand, self.game, actions=[{'type':'PLAY'}], includeActions=includeActions)
        ongoingJSON = GetCardListJSON(self.player.ongoing, self.game, source=ONGOING, includeActions=includeActions)
        discardPileJSON = GetCardListJSON(self.player.deck.discardPile, self.game, includeActions=includeActions)
        characterJSON = GameCharacterWrapper(self.player.character, self.game).toJSON(includeActions=includeActions)
        
        return {'ongoing':ongoingJSON,
                'name':self.player.name,
                'character':characterJSON,
                'pending':self.getPendingAction(),
                'isTurn':self.player is self.game.currentTurn.player,
                'deck':{'count':len(self.player.deck),
                        'hidden':True},
                'discardPile':{'cards':discardPileJSON, 'count':len(discardPileJSON)},
                'hand':{'count':len(self.player.hand),
                           'hidden':True}}
                
    def toJSONForYourself(self, includeActions=False):
        """ Return the Player as a JSON Dictionary as if you are this player """
        handJSON = GetCardListJSON(self.player.hand, self.game, actions=[{'type':'PLAY'}], includeActions=includeActions)
        json = self.toJSON(includeActions=includeActions)
        json['hand'] = handJSON
        
        return json
        
    def getPendingAction(self):
        """ Return the pending action """
        pendingAction = None
        if self.requestWrapper is not None:
            pendingAction = self.requestWrapper.PENDING_MESSAGE
        return pendingAction