
class AddTrigger:
    """ Represents an effect that adds a trigger to the current turn """
    
    def __init__(self, trigger):
        """ Initialize the add trigger effect with the trigger to add """
        self.trigger = trigger
        
    def perform(self, context):
        """ Perform the Game Effect """
        self.trigger.parent = context.parent
        context.owner.registerTrigger(self.trigger)