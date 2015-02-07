from card_wrapper import GetCardListJSON
from Server.Game.Actions.activate_action_builder import ActivateActionBuilder
from Game.Zones.zone_types import PLAYED

class PlayedCardsWrapper:
    """ A Wrapper to convert the plyed cards into JSON """
    
    def __init__(self, playedCards, game):
        """ Initialize the Turn Wrapper """
        self.playedCards = playedCards
        self.game = game
        
    def toJSON(self, includeActions=False):
        """ Return the turn as a JSON Dictionary """
        playedCardsJSON = GetCardListJSON(self.playedCards, actionBuilders=[ActivateActionBuilder(PLAYED, self.game)], includeActions=includeActions)
        activatableIndices = [self.playedCards.index(card) for card in self.playedCards if card in self.game.currentTurn.activatableEffects]
        
        return {'cards':playedCardsJSON, 
                'activatableIndices':activatableIndices}