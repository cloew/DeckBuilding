
class NotificationWrapper:
    """ Wrapper for a Game Notification to handle its conversion to JSON """
    
    def __init__(self, notification, game, requestingPlayer):
        """ Initialize the Notification Wrapper """
        self.notification = notification
        self.game = game
        self.requestingPlayer = requestingPlayer
        
    def toJSON(self):
        """ Return the Notification as JSON """
        return {"type":self.notification.notificationType,
                "id":self.game.notificationTracker.indexOf(self.notification)+1,
                "name":self.notification.player.name,
                "isYou":self.notification.player is self.requestingPlayer}