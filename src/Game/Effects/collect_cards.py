from Game.Effects.effect_runner import PerformEffects
from Game.Events.cards_event import CardsEvent
from Game.Sources.source_factory import SourceFactory, DECK

class CollectCards:
    """ Represents an effect to Collect Cards from the top of your opponents decks """
    
    def __init__(self, thenEffects, sourceType=None):
        """ Initialize the Effect with the effects to call with the collected cards """
        self.thenEffects = thenEffects
        if sourceType is None:
            sourceType = DECK
        self.sourceType = sourceType
        
    def perform(self, args):
        """ Perform the Game Effect """
        collectedCards = [SourceFactory.getSourceForEffect(self.sourceType, args.copyForPlayer(foe))[0] for foe in args.foes]
                
        event = CardsEvent(collectedCards, None, args)
        coroutine = PerformEffects(self.thenEffects, event.args)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)