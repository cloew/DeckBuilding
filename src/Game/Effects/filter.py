from Game.Commands.Requests.pick_card_request import PickCardRequest
from Game.Effects.effect_runner import PerformEffects
from Game.Events.cards_event import CardsEvent
from Game.Sources.source_factory import SourceFactory

class Filter:
    """ Represents an effect to pick cards from a source and an optional filter """
    
    def __init__(self, sourceType, filter, thenEffects):
        """ Initialize the options """
        self.sourceType = sourceType
        self.filter = filter
        self.thenEffects = thenEffects
        
    def perform(self, args):
        """ Perform the Game Effect """
        source = SourceFactory.getSourceForEffect(self.sourceType, args)
        possibleCards = self.filter.evaluate(args)
                
        event = CardsEvent(possibleCards, source, args)
        coroutine = PerformEffects(self.thenEffects, event.args)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)