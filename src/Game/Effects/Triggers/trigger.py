from Game.Effects.effect_runner import PerformEffect

class Trigger:
    """ Represents a Triggerable Effect """
    
    def __init__(self, subject, condition, effect, singleUse=False):
        """ Initialize the Trigger """
        self.subject = subject
        self.condition = condition
        self.effect = effect
        self.singleUse = singleUse
        
    def receive(self, event):
        """ Receive the event """
        if self.condition.evaluate(event.args.game, event=event):
            coroutine = PerformEffect(self.effect, event.args)
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response)
        
            if self.singleUse:
                event.args.owner.unregisterTrigger(self)