
class Notification:
    """ Represents a Game Notification for all players to see """
    
    def __init__(self, notificationType, player):
        """ Initialize the Notification with the player that caused it and the notification type """
        self.player = player
        self.notificationType = notificationType