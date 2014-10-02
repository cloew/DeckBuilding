from Game.Commands.Requests.choose_option_request import ChooseOptionRequest
from Game.Effects.effect_runner import PerformEffects
from Game.Sources.source_factory import SourceFactory

class Option:
    """ Represents an option for a Choice Effect """
    
    def __init__(self, description, effects):
        """ Initialize the Option """
        self.description = description
        self.effects = effects
        
    def performEffects(self, context):
        """ Perform the Option's Effects """
        coroutine = PerformEffects(self.effects, context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)

class Choice:
    """ Represents an effect absed on a choice """
    
    def __init__(self, options, relevantSourceType=None, filter=None):
        """ Initialize the options """
        self.options = options
        self.relevantSourceType = relevantSourceType
        self.filter = filter
        
    def perform(self, context):
        """ Perform the Game Effect """
        option = yield ChooseOptionRequest(self.options, context.player, self.findPossibleCards(context))
        coroutine = option.performEffects(context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)
                
    def findPossibleCards(self, context):
        """ Return the possible cards """
        possibleCards = None
        if self.relevantSourceType is not None:
            source = SourceFactory.getSourceForEffect(self.relevantSourceType, context)
            possibleCards = source
            if self.filter is not None:
                possibleCards = self.filter.evaluate(context)
        
        return possibleCards