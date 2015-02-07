from Server.Game.card_wrapper import GetCardListJSON
from Server.Game.Notifications.notification_wrapper import NotificationWrapper

class CardsNotificationWrapper(NotificationWrapper):
    """ Wrapper for a Game Notification to handle its conversion to JSON """
        
    def toJSON(self):
        """ Return the Notification as JSON """
        json = NotificationWrapper.toJSON(self)
        json["cards"] = GetCardListJSON(self.notification.cards)
        return json