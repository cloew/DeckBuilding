
class ChooseOptionRequestWrapper:
    """ A Wrapper for a Choose Option Request that handles its conversion to and from JSON """
    
    def __init__(self, request):
        """ Initialize the Request Wrapper """
        self.request = request
        
    def toJSON(self):
        """ Return the request as a JSON Dictionary """
        return {'type':'CHOICE',
                'options':[option.description for option in self.request.options]}