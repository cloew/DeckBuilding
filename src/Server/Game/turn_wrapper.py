from card_wrapper import CardWrapper
from json_helper import GetCardListJSON

class TurnWrapper:
    """ A Wrapper for a Game Turn """
    
    def __init__(self, turn):
        """ Initialize the Turn Wrapper """
        self.turn = turn
        
    def toJSON(self):
        """ Return the turn as a JSON Dictionary """
        handJSON = GetCardListJSON(self.turn.player.hand, actions=[{'type':'PLAY'}])
        playedJSON = GetCardListJSON(self.turn.playedCards)
        ongoingJSON = GetCardListJSON(self.turn.player.ongoing)
        discardPileJSON = GetCardListJSON(self.turn.player.deck.discardPile)
        
        return {'hand':handJSON,
                'played':playedJSON,
                'ongoing':ongoingJSON,
                'deck':{'count':len(self.turn.player.deck),
                        'hidden':True},
                'discardPile':{'cards':discardPileJSON},
                'power':self.turn.power}