from games import games

from card_wrapper import CardWrapper
from turn_wrapper import TurnWrapper

from Server.Game.Requests.choose_option_request_wrapper import ChooseOptionRequestWrapper

class GameWrapper:
    """ A Wrapper for a Game that handles its conversion to and from JSON """
    
    def __init__(self, game=None, id=None):
        """ Initialize the Game Wrapper """
        if id is not None:
            game = games[id]
        self.id = id
        self.game = game
        
    def toJSON(self):
        """ Return the game as a JSON Dictionary """
        kicksJSON = self.getCardListJSON(self.game.kickDeck)
        destroyedJSON = self.getCardListJSON(self.game.destroyedDeck)
        lineUpJSON = self.getCardListJSON(self.game.lineUp.cards)
        
        gameJSON = {'id':self.id,
                    'mainDeck':{'count':len(self.game.mainDeck),
                                'hidden':True},
                    'kicks':{'cards':kicksJSON},
                    'destroyed':{'cards':destroyedJSON},
                    'lineUp':lineUpJSON,
                    'turn':TurnWrapper(self.game.currentTurn).toJSON()}
                    
        if self.game.currentTurn.request is not None:
            gameJSON['request'] = ChooseOptionRequestWrapper(self.game.currentTurn.request).toJSON()
                    
        return {'game':gameJSON}
        
    def getCardListJSON(self, cards):
        """ Return the Card JSON for the given list of cards """
        return [CardWrapper(card).toJSON() for card in cards]