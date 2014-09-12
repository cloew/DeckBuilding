from Game.Commands.Requests.choose_option_request import ChooseOptionRequest
from Game.Effects.effect_runner import PerformEffects

class Option:
    """ Represents an option for a Choice Effect """
    
    def __init__(self, description, effects):
        """ Initialize the Option """
        self.description = description
        self.effects = effects
        
    def performEffects(self, args):
        """ Perform the Option's Effects """
        coroutine = PerformEffects(self.effects, args)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)

class Choice:
    """ Represents an effect absed on a choice """
    
    def __init__(self, options):
        """ Initialize the options """
        self.options = options
        
    def perform(self, args):
        """ Perform the Game Effect """
        option = yield ChooseOptionRequest(self.options)
        coroutine = option.performEffects()
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)