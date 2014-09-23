from card_wrapper import CardWrapper
from game_character_wrapper import GameCharacterWrapper
from json_helper import GetCardListJSON

from Game.Sources.source_factory import ONGOING, PLAYED

class PlayerWrapper:
    """ A Wrapper for a Game Player """
    
    def __init__(self, player, game):
        """ Initialize the Player Wrapper """
        self.player = player
        self.game = game
        
    def toJSON(self, includeActions=False):
        """ Return the Player as a JSON Dictionary """
        handJSON = GetCardListJSON(self.player.hand, self.game, actions=[{'type':'PLAY'}], includeActions=includeActions)
        ongoingJSON = GetCardListJSON(self.player.ongoing, self.game, source=ONGOING, includeActions=includeActions)
        discardPileJSON = GetCardListJSON(self.player.deck.discardPile, self.game, includeActions=includeActions)
        characterJSON = GameCharacterWrapper(self.player.character, self.game).toJSON()
        
        return {'ongoing':ongoingJSON,
                'character':characterJSON,
                'deck':{'count':len(self.player.deck),
                        'hidden':True},
                'discardPile':{'cards':discardPileJSON}}
                
    def toJSONForYourself(self, includeActions=False):
        """ Return the Player as a JSON Dictionary as if you are this player """
        handJSON = GetCardListJSON(self.player.hand, self.game, actions=[{'type':'PLAY'}], includeActions=includeActions)
        json = self.toJSON(includeActions=includeActions)
        json['hand'] = handJSON
        
        return json