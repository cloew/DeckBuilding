from Server.Game.json_helper import GetCardListJSON
from Server.Game.Notifications.cards_notification_wrapper import CardsNotificationWrapper

class RevealNotificationWrapper(CardsNotificationWrapper):
    """ Wrapper for a Game Notification to handle its conversion to JSON """
        
    def toJSON(self):
        """ Return the Notification as JSON """
        json = CardsNotificationWrapper.toJSON(self)
        json["zoneType"] = self.notification.zoneType
        return json