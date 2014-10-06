
class NotificationWrapper:
    """ Wrapper for a GameNotification to handle its conversion to JSON """
    
    def __init__(self, notification, requestingPlayer):
        """ Initialize the Notification Wrapper """
        self.notification = notification
        self.requestingPlayer = requestingPlayer
        
    def toJSON(self):
        """ Return the Notification as JSON """
        return {"type":self.notification.notificationType,
                "name":self.notification.player.name,
                "isYou":self.notification.player is self.requestingPlayer}