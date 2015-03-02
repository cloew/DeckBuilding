from Game.Zones.zone_factory import ZoneFactory

from contextlib import contextmanager

class Context:
    """ Represents a Game Context """
    
    def __init__(self, game, parent, event=None):
        """ Initialize the Arguments """
        self.parent = parent
        self.game = game
        self.event = event
        self.failed = False
        
    @property
    def owner(self):
        """ Return the owner aka the current turn """
        return self.game.currentTurn
        
    @property
    def notificationTracker(self):
        """ Return the notificationTracker for the game """
        return self.game.notificationTracker
    
    def addNotification(self, notification):
        """ Add a Game Notification """
        return self.notificationTracker.append(notification)
    
    @contextmanager
    def pushNotification(self, notification):
        """ Push a Game Notification onto the hierarchy """
        with self.notificationTracker.push(notification):
            yield
    
    def loadZone(self, zoneType):
        """ Load the given zone using this context """
        return ZoneFactory.getZoneInContext(zoneType, self)
    
    def sendEvent(self, event):
        """ Send a Game Event """
        return self.owner.ongoingEffects.send(event)
