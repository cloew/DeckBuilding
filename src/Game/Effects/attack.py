from Game.Commands.Requests.defend_request import DefendRequest
from Game.Effects.effect_runner import PerformEffects
from Game.Events.cards_event import CardsEvent
from Game.Notifications.notification import Notification, HIT_BY_ATTACK
from Game.Sources.source_factory import HAND

class Attack:
    """ Represents an effect to Attack other Players """
    
    def __init__(self, thenEffects):
        """ Initialize with the effects to attack with """
        self.thenEffects = thenEffects
        
    def perform(self, context):
        """ Perform the Game Effect """
        targets = []
        for foe in context.foes:
            defended = yield DefendRequest(context.parent, context.getPlayerContext(foe))
            if not defended:
                targets.append(foe)
                context.addNotification(Notification(HIT_BY_ATTACK, foe))
            else:
                playerContext = context.getPlayerContext(foe)
                source = playerContext.loadSource(HAND)
                event = CardsEvent([defended], source, playerContext)
                
                coroutine = PerformEffects(defended.defenseEffects, event.context)
                try:
                    response = yield coroutine.next()
                    while True:
                        response = yield coroutine.send(response)
                except StopIteration:
                    pass
                
        context = context.copy()
        context.foes = targets
        coroutine = PerformEffects(self.thenEffects, context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)