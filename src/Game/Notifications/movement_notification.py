from cards_notification import CardsNotification

class MovementNotification(CardsNotification):
    """ Represents a Game Notification that has some relevant Cards """
    
    def __init__(self, notificationType, player, fromZone, toZone):
        """ Initialize the Notification with the cards, the player that caused it and the notification type """
        self.fromZone = fromZone
        self.toZone = toZone
        CardsNotification.__init__(self, notificationType, player, list(fromZone), private=self.isPrivate(fromZone, toZone))
            
    def isPrivate(self, fromZone, toZone):
        """ Return if the gained card event is private """
        return not (fromZone.public or toZone.public)