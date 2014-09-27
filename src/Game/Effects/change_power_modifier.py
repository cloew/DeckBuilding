
class ChangePowerModifier:
    """ Represents an effect that chagnes the turn's power modifier """
    
    def __init__(self, modifier):
        """ Initialize the Effect with the modifier to add """
        self.modifier = modifier
        
    def perform(self, args):
        """ Perform the Game Effect """
        args.owner.changeModifier(self.modifier)