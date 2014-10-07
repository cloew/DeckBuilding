
class NotificationTracker:
    """ Represents the colletion of notifications the game has generated """
    MAX_NOTIFICATIONS = 10
    
    def __init__(self):
        """ Initialize the Notification Tracker """
        self.notifications = []
        self.append = self.notifications.append
        self.indexOf = self.notifications.index
        
    @property
    def latestNotifications(self):
        """ Return the notifications from most recent to least recent """
        latestNotifications = list(self.notifications)
        latestNotifications.reverse()
        return latestNotifications[:self.MAX_NOTIFICATIONS]