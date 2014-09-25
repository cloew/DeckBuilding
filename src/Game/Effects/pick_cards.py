from Game.Commands.Requests.pick_card_request import PickCardRequest
from Game.Effects.effect_runner import PerformEffect
from Game.Events.cards_event import CardsEvent
from Game.Sources.source_factory import SourceFactory

class PickCards:
    """ Represents an effect to pick cards from a source and an optional filter """
    
    def __init__(self, sourceType, numberOfCards, thenEffect, filter=None):
        """ Initialize the options """
        self.sourceType = sourceType
        self.numberOfCards = numberOfCards
        self.thenEffect = thenEffect
        self.filter = filter
        
    def perform(self, args):
        """ Perform the Game Effect """
        source = SourceFactory.getSourceForEffect(self.sourceType, args)
        possibleCards = source
        if self.filter is not None:
            possibleCards = self.filter.evaluate(args)
        
        card = None
        if len(possibleCards) == self.numberOfCards:
            cards = possibleCards
        else:
            cards = yield PickCardRequest(possibleCards, args.player, self.numberOfCards)
            
        event = CardsEvent(cards, source, args)
        coroutine = PerformEffect(self.thenEffect, event.args)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)