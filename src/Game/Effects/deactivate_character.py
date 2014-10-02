
class DeactivateCharacter:
    """ Represents an effect to Deactivate the Player's Character """
        
    def perform(self, context):
        """ Perform the Game Effect """
        context.player.character.deactivate()