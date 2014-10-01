
class AddActivatable:
    """ Represents an effect that adds a activatable to the current turn """
    
    def __init__(self, activatable):
        """ Initialize the add activatable effect with the activatable to add """
        self.activatable = activatable
        
    def perform(self, args):
        """ Perform the Game Effect """
        args.owner.registerActivatable(args.parent, self.activatable)