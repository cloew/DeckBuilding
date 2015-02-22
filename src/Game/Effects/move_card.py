from Game.Effects.effect_runner import RunCoroutineOrFunction
from Game.Effects.Conditions.Filters.cards_finder import CardsFinder

class MoveCard:
    """ Represents an effect to Move a Card """
    
    def __init__(self, fromZoneType, toZoneType, filter=None):
        """ Initialize the Effect """
        self.fromZoneType = fromZoneType
        self.toZoneType = toZoneType
        self.cardsFinder = CardsFinder(fromZoneType, filter)
        
    def perform(self, context):
        """ Perform the Game Effect """
        fromZone = self.cardsFinder.findAsEvent(context)
        toZone = context.loadZone(self.toZoneType)
        
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
        return None
        
    def afterMove(self, context, fromZone, toZone):
        """ Perform any actions after the move """