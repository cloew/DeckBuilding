from Game.Effects.effect_runner import RunCoroutineOrFunction
from Game.Effects.Conditions.Filters.cards_finder import CardsFinder
from Game.Notifications.movement_notification import MovementNotification
from Game.Notifications.notification_types import MOVED_CARD

from smart_defaults import smart_defaults, EvenIfNone

class MoveCard:
    """ Represents an effect to Move a Card """
    
    @smart_defaults
    def __init__(self, fromZoneType, toZoneType, filter=None, notificationType=EvenIfNone(MOVED_CARD)):
        """ Initialize the Effect """
        self.fromZoneType = fromZoneType
        self.toZoneType = toZoneType
        self.notificationType = notificationType
        self.cardsFinder = CardsFinder(fromZoneType, filter)
        
    def perform(self, context):
        """ Perform the Game Effect """
        fromZone = self.cardsFinder.findAsEvent(context)
        toZone = context.loadZone(self.toZoneType)
        
        if len(fromZone) > 0:
            self.moveCards(fromZone, toZone)
            coroutine = RunCoroutineOrFunction(self.afterMove, context, fromZone, toZone)
            try:
                response = yield coroutine.next()
                while True:
                    response = yield coroutine.send(response)
            except StopIteration:
                pass
            self.addNotification(context, fromZone, toZone)
        
    def moveCards(self, fromZone, toZone):
        for card in list(fromZone):
            fromZone.remove(card)
            toZone.add(card)
            
    def addNotification(self, context, fromZone, toZone):
        """ Add the Notification """
        notification = self.getNotification(context, fromZone, toZone)
        if notification is not None:
            context.addNotification(notification)
        
    def getNotification(self, context, fromZone, toZone):
        """ Return the notification to use for the movement """
        return MovementNotification(self.notificationType, context.player, fromZone, toZone)
        
    def afterMove(self, context, fromZone, toZone):
        """ Perform any actions after the move """