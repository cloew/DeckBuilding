from Game.Notifications.cards_notification import CardsNotification
from Game.Notifications.notification import Notification
from Game.Notifications.reveal_notification import RevealNotification

from Server.Game.Notifications.cards_notification_wrapper import CardsNotificationWrapper
from Server.Game.Notifications.notification_wrapper import NotificationWrapper
from Server.Game.Notifications.reveal_notification_wrapper import RevealNotificationWrapper

class NotificationWrapperFactory:
    """ Factory to construct Request Wrappers """
    NOTIFICATION_TO_WRAPPER = {CardsNotification:CardsNotificationWrapper,
                               Notification:NotificationWrapper,
                               RevealNotification:RevealNotificationWrapper}
    
    def buildWrapper(self, notification, game, requestingPlayer):
        """ Return the current Request Wrapper """
        if notification.__class__ in self.NOTIFICATION_TO_WRAPPER:
            return self.NOTIFICATION_TO_WRAPPER[notification.__class__](notification, game, requestingPlayer)
            
NotificationWrapperFactory = NotificationWrapperFactory()