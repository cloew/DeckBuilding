from Server.Game.card_wrapper import GetCardListJSON

class ChooseOptionRequestWrapper:
    """ A Wrapper for a Choose Option Request that handles its conversion to JSON """
    PENDING_MESSAGE = "Making a choice"
    
    def __init__(self, id, request, game):
        """ Initialize the Request Wrapper """
        self.id = id
        self.request = request
        self.game = game
        
    def toJSON(self, includeActions=False):
        """ Return the request as a JSON Dictionary """
        cards = []
        relevantCards = self.request.relevantCards
        if relevantCards is not None:
            cards = GetCardListJSON(relevantCards, includeActions=includeActions)
        return {'type':'CHOICE',
                'id':self.id,
                'options':[option.description for option in self.request.options],
                'cards':cards}