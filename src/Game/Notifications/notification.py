
class Notification:
    """ Represents a Game Notification for all players to see """
    
    def __init__(self, player, message):
        """ Initialize the Notification with the player that caused it and the notification message """
        self.player = player
        self.message = message