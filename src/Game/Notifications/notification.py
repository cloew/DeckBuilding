from helpers.incrementer import Incrementer

notificationIdProvider = Incrementer(startAt=1)

class Notification:
    """ Represents a Game Notification for all players to see """
    
    def __init__(self, notificationType, player):
        """ Initialize the Notification with the player that caused it and the notification type """
        self.id = notificationIdProvider.next()
        self.player = player
        self.notificationType = notificationType
        self.notifications = []
        
    def addChild(self, notification):
        """ Add child notification """
        self.notifications.append(notification)
        
    def __repr__(self):
        """ Return the string representation of the notification """
        return "<{0} at {1:#x}>".format(self.notificationType, id(self))