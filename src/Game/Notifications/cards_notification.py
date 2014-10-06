from notification import Notification

DEFENDED = "DEFENDED"

class CardsNotification(Notification):
    """ Represents a Game Notification that has some relevant Cards """
    
    def __init__(self, notificationType, player, cards):
        """ Initialize the Notification with the cards, the player that caused it and the notification type """
        self.cards = cards
        Notification.__init__(self, notificationType, player)