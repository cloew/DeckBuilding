from json_helper import GetCardListJSON
from Game.Zones.zone_types import PLAYED

class TurnWrapper:
    """ A Wrapper for a Game Turn """
    
    def __init__(self, turn):
        """ Initialize the Turn Wrapper """
        self.turn = turn
        
    def toJSON(self, includeActions=False):
        """ Return the turn as a JSON Dictionary """
        playedCardsJSON = GetCardListJSON(self.turn.playedCards, self.turn.game, zone=PLAYED, includeActions=includeActions)
        
        return {'played':{'cards':playedCardsJSON, 'activatableIndices':[self.turn.playedCards.index(card) for card in self.turn.playedCards if card in self.turn.game.currentTurn.activatableEffects]},
                'power':self.turn.power,
                'modifier':self.turn.modifier,
                'playerName':self.turn.player.name,
                'canEndTurn':includeActions}