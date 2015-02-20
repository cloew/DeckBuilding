from notification import Notification

class CardsNotification(Notification):
    """ Represents a Game Notification that has some relevant Cards """
    
    def __init__(self, notificationType, player, cards, private=False):
        """ Initialize the Notification with the cards, the player that caused it and the notification type """
        self.cards = cards
        self.private = private
        Notification.__init__(self, notificationType, player)