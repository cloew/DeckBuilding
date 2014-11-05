
class IsPlayerCharacter:
    """ Represents a condition where the context parent must be the player's character """
        
    def evaluate(self, context):
        """ Evaluate the condition """
        return context.player.character is context.parent