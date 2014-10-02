from Server.Game.json_helper import GetCardListJSON

class ChooseOptionRequestWrapper:
    """ A Wrapper for a Choose Option Request that handles its conversion to JSON """
    
    def __init__(self, request, game):
        """ Initialize the Request Wrapper """
        self.request = request
        self.game = game
        
    def toJSON(self, includeActions=False):
        """ Return the request as a JSON Dictionary """
        cards = []
        relevantCards = self.request.relevantCards
        if relevantCards is not None:
            cards = GetCardListJSON(relevantCards, self.game, includeActions=includeActions)
        return {'type':'CHOICE',
                'options':[option.description for option in self.request.options],
                'cards':cards}