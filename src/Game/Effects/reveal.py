from Game.Notifications.reveal_notification import RevealNotification

class Reveal:
    """ Represents an effect to Reveal Cards """
    
    def __init__(self, zoneType):
        """ Initialize the Effect with the number of cards to draw """
        self.zoneType = zoneType
        
    def perform(self, context):
        """ Perform the Game Effect """
        zone = context.loadZone(self.zoneType)
        context.addNotification(RevealNotification(context.player, zone))