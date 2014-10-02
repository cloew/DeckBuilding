
class ChangePowerModifier:
    """ Represents an effect that chagnes the turn's power modifier """
    
    def __init__(self, modifier):
        """ Initialize the Effect with the modifier to add """
        self.modifier = modifier
        
    def perform(self, context):
        """ Perform the Game Effect """
        context.owner.changeModifier(self.modifier)