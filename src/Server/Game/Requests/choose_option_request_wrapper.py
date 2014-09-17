from Server.Game.json_helper import GetCardListJSON

class ChooseOptionRequestWrapper:
    """ A Wrapper for a Choose Option Request that handles its conversion to JSON """
    
    def __init__(self, request, game):
        """ Initialize the Request Wrapper """
        self.request = request
        self.game = game
        
    def toJSON(self):
        """ Return the request as a JSON Dictionary """
        cards = []
        relevantSource = self.request.relevantSource
        if relevantSource is not None:
            cards = GetCardListJSON(relevantSource, self.game)
        return {'type':'CHOICE',
                'options':[option.description for option in self.request.options],
                'cards':cards}