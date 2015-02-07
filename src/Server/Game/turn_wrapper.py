from played_cards_wrapper import PlayedCardsWrapper

class TurnWrapper:
    """ A Wrapper for a Game Turn """
    
    def __init__(self, turn):
        """ Initialize the Turn Wrapper """
        self.turn = turn
        
    def toJSON(self, includeActions=False):
        """ Return the turn as a JSON Dictionary """
        return {'played':PlayedCardsWrapper(self.turn.playedCards, self.turn.game).toJSON(includeActions=includeActions),
                'power':self.turn.power,
                'modifier':self.turn.modifier,
                'playerName':self.turn.player.name,
                'canEndTurn':includeActions}