
class AddTrigger:
    """ Represents an effect that adds a trigger to the current turn """
    
    def __init__(self, trigger):
        """ Initialize the add trigger effect with the trigger to add """
        self.trigger = trigger
        
    def perform(self, args):
        """ Perform the Game Effect """
        args.owner.registerTrigger(self.trigger)