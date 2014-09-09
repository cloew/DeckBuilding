
class Trigger:
    """ Represents a Triggerable Effect """
    
    def __init__(self, subject, effect, singleUse=False):
        """ Initialize the Trigger """
        self.subject = subject
        self.effect = effect
        self.singleUse = singleUse
        
    def receive(self, event):
        """ Receive the event """
        self.effect.perform(event.args)
        
        if self.singleUse:
            event.args.owner.unregisterTrigger(self)