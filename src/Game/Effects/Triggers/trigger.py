from Game.Effects.effect_runner import PerformEffect

class Trigger:
    """ Represents a Triggerable Effect """
    
    def __init__(self, subject, effect, condition=None, singleUse=False):
        """ Initialize the Trigger """
        self.subject = subject
        self.condition = condition
        self.effect = effect
        self.singleUse = singleUse
        
    def receive(self, event):
        """ Receive the event """
        if self.condition is None or self.condition.evaluate(event.context):
            if self.singleUse:
                event.context.owner.unregisterTrigger(self)
        
            coroutine = PerformEffect(self.effect, event.context)
            try:
                response = yield coroutine.next()
                while True:
                    response = yield coroutine.send(response)
            except StopIteration:
                pass