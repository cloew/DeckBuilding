from json_helper import GetCardListJSON
from Game.Zones.zone_types import PLAYED

class PlayedCardsWrapper:
    """ A Wrapper to convert the plyed cards into JSON """
    
    def __init__(self, playedCards, game):
        """ Initialize the Turn Wrapper """
        self.playedCards = playedCards
        self.game = game
        
    def toJSON(self, includeActions=False):
        """ Return the turn as a JSON Dictionary """
        playedCardsJSON = GetCardListJSON(self.playedCards, self.game, zone=PLAYED, includeActions=includeActions)
        activatableIndices = [self.playedCards.index(card) for card in self.playedCards if card in self.game.currentTurn.activatableEffects]
        
        return {'cards':playedCardsJSON, 
                'activatableIndices':activatableIndices}