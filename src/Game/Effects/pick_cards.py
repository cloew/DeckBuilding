from Game.Commands.Requests.pick_card_request import PickCardRequest
from Game.Effects.effect_runner import PerformEffect
from Game.Events.cards_event import CardsEvent
from Game.Sources.source_factory import SourceFactory

class PickCards:
    """ Represents an effect to pick cards from a source and an optional filter """
    REQUEST_CLASS = PickCardRequest
    AUTO_PICK = True
    
    def __init__(self, sourceType, numberOfCards, thenEffect, filter=None):
        """ Initialize the options """
        self.sourceType = sourceType
        self.numberOfCards = numberOfCards
        self.thenEffect = thenEffect
        self.filter = filter
        
    def perform(self, args):
        """ Perform the Game Effect """
        source, possibleCards = self.findPossibleCards(args)
        
        if len(possibleCards) != 0:
            card = None
            if len(possibleCards) == self.numberOfCards and self.AUTO_PICK:
                cards = possibleCards
            else:
                cards = yield self.REQUEST_CLASS(possibleCards, args.player, self.numberOfCards)
                
            event = CardsEvent(cards, source, args)
            coroutine = PerformEffect(self.thenEffect, event.args)
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response)
                
    def findPossibleCards(self, args):
        """ Return the possible cards """
        source = SourceFactory.getSourceForEffect(self.sourceType, args)
        possibleCards = source
        if self.filter is not None:
            possibleCards = self.filter.evaluate(args)
        
        return source, possibleCards
        
    def setNumberOfCards(self, number):
        """ Set the Number of Cards that can be requested """
        self.numberOfCards = number