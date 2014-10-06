
class NotificationTracker:
    """ Represents the colletion of notifications the game has generated """
    
    def __init__(self):
        """ Initialize the Notification Tracker """
        self.notifications = []
        self.append = self.notifications.append