from Game.Effects.effect_runner import PerformEffect

class ConditionalEffect:
    """ Represents an effect that conditionally applies """
    
    def __init__(self, condition, effect):
        """ Initialize the Effect with the condition to evaluate and effect to perform """
        self.condition = condition
        self.effect = effect
        
    def perform(self, args):
        """ Perform the Game Effect """
        if self.condition.evaluate(args.game, event=args.event):
            coroutine = PerformEffect(self.effect, args)
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response) 