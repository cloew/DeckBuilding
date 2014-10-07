from Game.Notifications.reveal_notification import RevealNotification

class Reveal:
    """ Represents an effect to Reveal Cards """
    
    def __init__(self, sourceType):
        """ Initialize the Effect with the number of cards to draw """
        self.sourceType = sourceType
        
    def perform(self, context):
        """ Perform the Game Effect """
        source = context.loadSource(self.sourceType)
        context.addNotification(RevealNotification(context.player, source))