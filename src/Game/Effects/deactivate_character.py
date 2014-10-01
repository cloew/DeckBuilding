
class DeactivateCharacter:
    """ Represents an effect to Deactivate the Player's Character """
        
    def perform(self, args):
        """ Perform the Game Effect """
        args.player.character.deactivate()