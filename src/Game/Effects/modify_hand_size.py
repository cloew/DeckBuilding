
class ModifyHandSize:
    """ Represents an effect to modify a Player's Hand Size """
    
    def __init__(self, change):
        """ Initialize the Effect with the amount to change a player's hand by """
        self.change = change
        
    def perform(self, context):
        """ Perform the Game Effect """
        context.player.modifyHandSize(self.change)