from Game.Effects.effect_runner import PerformEffect

class ConditionalEffect:
    """ Represents an effect that conditionally applies """
    
    def __init__(self, condition, effect, otherwiseEffect=None):
        """ Initialize the Effect with the condition to evaluate and effect to perform """
        self.condition = condition
        self.effect = effect
        self.otherwiseEffect = otherwiseEffect
        
    def perform(self, context):
        """ Perform the Game Effect """
        coroutine = None
        if self.condition.evaluate(context):
            coroutine = self.performEffect(context)
        elif self.otherwiseEffect is not None:
            coroutine = self.performOtherwiseEffect(context)
            
        if coroutine is not None:
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response)
                
    def performEffect(self, context):
        """ Perform the conditional effect """
        coroutine = PerformEffect(self.effect, context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)
            
    def performOtherwiseEffect(self, context):
        """ Perform the conditional effect """
        coroutine = PerformEffect(self.otherwiseEffect, context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)