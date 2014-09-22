from card_wrapper import CardWrapper
from character_wrapper import CharacterWrapper
from json_helper import GetCardListJSON

from Game.Sources.source_factory import ONGOING, PLAYED

class TurnWrapper:
    """ A Wrapper for a Game Turn """
    
    def __init__(self, turn):
        """ Initialize the Turn Wrapper """
        self.turn = turn
        
    def toJSON(self, includeActions=False):
        """ Return the turn as a JSON Dictionary """
        handJSON = GetCardListJSON(self.turn.player.hand, self.turn.game, actions=[{'type':'PLAY'}], includeActions=includeActions)
        playedJSON = GetCardListJSON(self.turn.playedCards, self.turn.game, source=PLAYED, includeActions=includeActions)
        ongoingJSON = GetCardListJSON(self.turn.player.ongoing, self.turn.game, source=ONGOING, includeActions=includeActions)
        discardPileJSON = GetCardListJSON(self.turn.player.deck.discardPile, self.turn.game, includeActions=includeActions)
        characterJSON = CharacterWrapper(self.turn.player.character, self.turn.game).toJSON()
        
        return {'hand':handJSON,
                'played':playedJSON,
                'ongoing':ongoingJSON,
                'character':characterJSON,
                'deck':{'count':len(self.turn.player.deck),
                        'hidden':True},
                'discardPile':{'cards':discardPileJSON},
                'power':self.turn.power}