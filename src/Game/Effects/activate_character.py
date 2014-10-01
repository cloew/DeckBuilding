
class ActivateCharacter:
    """ Represents an effect to Activate the Player's Character """
        
    def perform(self, args):
        """ Perform the Game Effect """
        args.player.character.activate(args.owner)