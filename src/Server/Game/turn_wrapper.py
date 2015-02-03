from json_helper import GetCardListJSON
from Game.Zones.zone_types import PLAYED

class TurnWrapper:
    """ A Wrapper for a Game Turn """
    
    def __init__(self, turn):
        """ Initialize the Turn Wrapper """
        self.turn = turn
        
    def toJSON(self, includeActions=False):
        """ Return the turn as a JSON Dictionary """
        playedJSON = GetCardListJSON(self.turn.playedCards, self.turn.game, zone=PLAYED, includeActions=includeActions)
        
        return {'played':playedJSON,
                'power':self.turn.power,
                'modifier':self.turn.modifier,
                'playerName':self.turn.player.name,
                'canEndTurn':includeActions}