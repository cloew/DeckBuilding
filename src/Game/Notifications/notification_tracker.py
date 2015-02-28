from contextlib import contextmanager

class NotificationTracker:
    """ Represents the colletion of notifications the game has generated """
    MAX_NOTIFICATIONS = 10
    
    def __init__(self):
        """ Initialize the Notification Tracker """
        self.notifications = []
        self.hierarchy = []
        self.indexOf = self.notifications.index
        
    def append(self, notification):
        """ Append the notification to the proper spot in the hierarchy """
        if len(self.hierarchy) == 0:
            self.notifications.append(notification)
        else:
            self.hierarchy[-1].addChild(notification)
        
    @property
    def latestNotifications(self):
        """ Return the notifications from most recent to least recent """
        latestNotifications = list(self.notifications)
        latestNotifications.reverse()
        return latestNotifications[:self.MAX_NOTIFICATIONS]
    
    @contextmanager
    def push(self, notification):
        """ Push the notification onto the notification hierarchy stack """
        try:
            self.hierarchy.append(notification)
            yield
        finally:
            self.hierarchy.remove(notification)