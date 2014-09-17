
class Activatable:
    """ Represents an effect that can be activated """
    
    def __init__(self, effect, singleUse=False):
        """ Initialize the Activatable Effect """
        self.effect = effect
        self.singleUse = singleUse
        
    def activate(self, args):
        """ Activate the effect """
        self.effect.perform(args)
        
        if self.singleUse:
            args.owner.unregisterActivatable(args.parent)