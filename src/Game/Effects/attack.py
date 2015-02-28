from Game.Commands.Requests.defend_request import DefendRequest
from Game.Effects.effect_runner import PerformEffects

from Game.Events.cards_event import CardsEvent
from Game.Events.defend_event import DefendEvent

from Game.Notifications.cards_notification import CardsNotification
from Game.Notifications.notification import Notification
from Game.Notifications.notification_types import ATTACKED, DEFENDED, HIT_BY_ATTACK
from Game.Zones.zone_types import HAND

class Attack:
    """ Represents an effect to Attack other Players """
    
    def __init__(self, thenEffects):
        """ Initialize with the effects to attack with """
        self.thenEffects = thenEffects
        
    def perform(self, context):
        """ Perform the Game Effect """
        attackNotification = CardsNotification(ATTACKED, context.player, [context.parent])
        context.addNotification(attackNotification)
        with context.pushNotification(attackNotification):
            coroutine = self.requestDefenses(context)
            try:
                response = yield coroutine.next()
                while True:
                    response = yield coroutine.send(response)
            except StopIteration:
                pass
                
            coroutine = self.attackTargets(context)
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response)
        
    def requestDefenses(self, context):
        """ Request defenses to determine who the targets are """
        self.targets = []
        self.failedAttacks = []
        for foe in context.foes:
            request = DefendRequest(context.parent, context.getPlayerContext(foe))
            defended = yield request
            if not defended:
                self.targets.append(foe)
                context.addNotification(Notification(HIT_BY_ATTACK, foe))
            else:
                self.failedAttacks.append(True)
                context.addNotification(CardsNotification(DEFENDED, foe, [defended]))
                playerContext = context.getPlayerContext(foe)
                
                coroutine = context.owner.ongoingEffects.send(DefendEvent(defended, playerContext))
                try:
                    response = yield coroutine.next()
                    while True:
                        response = yield coroutine.send(response)
                except StopIteration:
                    pass
                
                zone = playerContext.loadZone(request.findZoneFor(defended))
                event = CardsEvent([defended], zone, playerContext)
                coroutine = PerformEffects(defended.defenseEffects, event.context)
                try:
                    response = yield coroutine.next()
                    while True:
                        response = yield coroutine.send(response)
                except StopIteration:
                    pass
                
    def attackTargets(self, context):
        """ Attack the Targets """
        context = context.copy()
        context.foes = self.targets
        coroutine = PerformEffects(self.thenEffects, context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)