from Game.Commands.Requests.choose_option_request import ChooseOptionRequest
from Game.Effects.effect_runner import PerformEffects

class Option:
    """ Represents an option for a Choice Effect """
    
    def __init__(self, description, effects, condition=None):
        """ Initialize the Option """
        self.description = description
        self.effects = effects
        self.condition = condition
        
    def performEffects(self, context):
        """ Perform the Option's Effects """
        coroutine = PerformEffects(self.effects, context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)
            
    def isAvailable(self, context):
        """ Check if the Option is available to be chosen """
        canChoose = True
        if self.condition is not None:
            return self.condition.evaluate(context)
        return True

class Choice:
    """ Represents an effect absed on a choice """
    
    def __init__(self, options, relevantZoneType=None, filter=None):
        """ Initialize the options """
        self.options = options
        self.relevantZoneType = relevantZoneType
        self.filter = filter
        
    def perform(self, context):
        """ Perform the Game Effect """
        availableOptions = [option for option in self.options if option.isAvailable(context)]
        if len(availableOptions) == 0:
            return
        elif len(availableOptions) == 1:
            option = availableOptions[0]
        else:
            option = yield ChooseOptionRequest(availableOptions, context.player, self.findPossibleCards(context))
            
        coroutine = option.performEffects(context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)
                
    def findPossibleCards(self, context):
        """ Return the possible cards """
        possibleCards = None
        if self.filter is not None:
            possibleCards = self.filter.evaluate(context)
        elif self.relevantZoneType is not None:
            source = context.loadZone(self.relevantZoneType)
            possibleCards = source
        
        return possibleCards