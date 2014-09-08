
class Trigger:
    """ Represents a Triggerable Effect """
    
    def __init__(self, subject, effect):
        """ Initialize the Trigger """
        self.subject = subject
        self.effect = effect
        
    def receive(self, event):
        """ Receive the event """
        self.effect.perform(event.args)