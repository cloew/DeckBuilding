from cards_notification import CardsNotification

REVEAL = "REVEAL"

class RevealNotification(CardsNotification):
    """ Represents a Game Notification that has some relevant Cards """
    
    def __init__(self, player, zone):
        """ Initialize the Notification with the cards, the player that caused it and the notification type """
        self.zoneType = zone.zoneType
        CardsNotification.__init__(self, REVEAL, player, zone)