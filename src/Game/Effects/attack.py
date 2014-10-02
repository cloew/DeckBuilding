from Game.Commands.Requests.defend_request import DefendRequest
from Game.Effects.effect_runner import PerformEffectsForEachPlayer, PerformEffects
from Game.Events.cards_event import CardsEvent
from Game.Sources.source_factory import SourceFactory, HAND

class Attack:
    """ Represents an effect to Attack other Players """
    
    def __init__(self, effect):
        """ Initialize with the effect to attack with """
        self.effects = [effect]
        
    def perform(self, args):
        """ Perform the Game Effect """
        targets = []
        for foe in args.foes:
            defended = yield DefendRequest(args.parent, foe, args)
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
                
        coroutine = PerformEffectsForEachPlayer(self.effects, targets, args)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)