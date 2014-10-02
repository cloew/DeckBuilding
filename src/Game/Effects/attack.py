from Game.Commands.Requests.defend_request import DefendRequest
from Game.Effects.effect_runner import PerformEffects
from Game.Events.cards_event import CardsEvent
from Game.Sources.source_factory import SourceFactory, HAND

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
            else:
                playerArgs = context.getPlayerContext(foe)
                source = SourceFactory.getSourceForEffect(HAND, playerArgs)
                event = CardsEvent([defended], source, playerArgs)
                
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