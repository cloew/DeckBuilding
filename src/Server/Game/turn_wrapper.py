from played_cards_wrapper import PlayedCardsWrapper

class TurnWrapper:
    """ A Wrapper for a Game Turn """
    
    def __init__(self, turn, game):
        """ Initialize the Turn Wrapper """
        self.turn = turn
        self.game = game
        
    def toJSON(self, playerId, includeActions=False):
        """ Return the turn as a JSON Dictionary """
        return {'played':PlayedCardsWrapper(self.turn.playedCards, self.game).toJSON(playerId, includeActions=includeActions),
                'power':self.turn.power,
                'modifier':self.turn.modifier,
                'playerName':self.turn.player.name,
                'canEndTurn':includeActions}