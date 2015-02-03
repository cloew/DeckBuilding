from Game.Effects.effect_runner import PerformEffect

class Trigger:
    """ Represents a Triggerable Effect """
    
    def __init__(self, subject, effect, condition=None, singleUse=False):
        """ Initialize the Trigger """
        self.subject = subject
        self.condition = condition
        self.effect = effect
        self.singleUse = singleUse
        self.parent = None
        
    def receive(self, event):
        """ Receive the event """
        context = self.getTriggerContext(event)
        if self.condition is None or self.condition.evaluate(context):
            if self.singleUse:
                context.owner.unregisterTrigger(self)
        
            coroutine = PerformEffect(self.effect, context)
            try:
                response = yield coroutine.next()
                while True:
                    response = yield coroutine.send(response)
            except StopIteration:
                pass
                
    def getTriggerContext(self, event):
        """ Return the modified context to specify the trigger zone as the parent """
        context = event.context.copy()
        context.parent = self.parent
        return context