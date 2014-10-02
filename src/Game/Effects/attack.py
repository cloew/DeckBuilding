from Game.Commands.Requests.defend_request import DefendRequest
from Game.Effects.effect_runner import PerformEffects
from Game.Events.cards_event import CardsEvent
from Game.Sources.source_factory import SourceFactory, HAND

class Attack:
    """ Represents an effect to Attack other Players """
    
    def __init__(self, thenEffects):
        """ Initialize with the effects to attack with """
        self.thenEffects = thenEffects
        
    def perform(self, args):
        """ Perform the Game Effect """
        targets = []
        for foe in args.foes:
            defended = yield DefendRequest(args.parent, args.copyForPlayer(foe))
            if not defended:
                targets.append(foe)
            else:
                playerArgs = args.copyForPlayer(foe)
                source = SourceFactory.getSourceForEffect(HAND, playerArgs)
                event = CardsEvent([defended], source, playerArgs)
                
                coroutine = PerformEffects(defended.defenseEffects, event.args)
                try:
                    response = yield coroutine.next()
                    while True:
                        response = yield coroutine.send(response)
                except StopIteration:
                    pass
                
        args = args.copy()
        args.foes = targets
        coroutine = PerformEffects(self.thenEffects, args)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)