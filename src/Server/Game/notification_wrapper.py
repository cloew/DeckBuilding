
class NotificationWrapper:
    """ Wrapper for a GameNotification to handle its conversion to JSON """
    
    def __init__(self, notification, requestingPlayer):
        """ Initialize the Notification Wrapper """
        self.notification = notification
        self.requestingPlayer = requestingPlayer
        
    def toJSON(self):
        """ Return the Notification as JSON """
        return {"message":self.getMessage()}
        
    def getMessage(self):
        """ Return the proper Notification message """
        name = self.notification.player.name
        if self.notification.player is self.requestingPlayer:
            name = "You"
        return "{0} {1}".format(name, self.notification.message)