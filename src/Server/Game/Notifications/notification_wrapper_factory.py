from Game.Commands.Notifications.notification import Notification

from Server.Game.Notifications.notification_wrapper import NotificationWrapper

class NotificationWrapperFactory:
    """ Factory to construct Request Wrappers """
    NOTIFICATION_TO_WRAPPER = {Notification:NotificationWrapper}
    
    def buildWrapper(self, notification, requestingPlayer):
        """ Return the current Request Wrapper """
        if notification.__class__ in self.NOTIFICATION_TO_WRAPPER:
            return self.NOTIFICATION_TO_WRAPPER[notification.__class__](notification, requestingPlayer)
            
NotificationWrapperFactory = NotificationWrapperFactory()