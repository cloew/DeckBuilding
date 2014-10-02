
class ActivateCharacter:
    """ Represents an effect to Activate the Player's Character """
        
    def perform(self, context):
        """ Perform the Game Effect """
        context.player.character.activate(context.owner)