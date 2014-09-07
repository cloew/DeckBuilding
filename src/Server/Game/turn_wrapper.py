from card_wrapper import CardWrapper

class TurnWrapper:
    """ A Wrapper for a Game Turn """
    
    def __init__(self, turn):
        """ Initialize the Turn Wrapper """
        self.turn = turn
        
    def toJSON(self):
        """ Return the turn as a JSON Dictionary """
        handJSON = [CardWrapper(card).toJSON() for card in self.turn.player.hand]
        playedJSON = [CardWrapper(card).toJSON() for card in self.turn.playedCards]
        ongoingJSON = [CardWrapper(card).toJSON() for card in self.turn.player.ongoing]
        
        return {'hand':handJSON,
                'played':playedJSON,
                'ongoing':ongoingJSON,
                'power':self.turn.power}