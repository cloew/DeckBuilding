from Game.Commands.Requests.pick_card_request import PickCardRequest
from Game.Effects.conditional_effect import ConditionalEffect
from Game.Effects.Conditions.has_cards import HasCards
from Game.Events.cards_event import CardsEvent

class PickCards(ConditionalEffect):
    """ Represents an effect to pick cards from a source and an optional filter """
    REQUEST_CLASS = PickCardRequest
    AUTO_PICK = True
    
    def __init__(self, sourceType, numberOfCards, thenEffects, filter=None):
        """ Initialize the options """
        self.sourceType = sourceType
        self.numberOfCards = numberOfCards
        self.filter = filter
        ConditionalEffect.__init__(self, HasCards(self.sourceType, filter=filter), thenEffects)
        
    def performEffects(self, context):
        """ Perform the Game Effect """
        source, possibleCards = self.findPossibleCards(context)
        
        if len(possibleCards) != 0:
            card = None
            if len(possibleCards) == self.numberOfCards and self.AUTO_PICK:
                cards = possibleCards
            else:
                cards = yield self.REQUEST_CLASS(possibleCards, context.player, self.numberOfCards)
                
            event = CardsEvent(cards, source, context)
        
        coroutine = ConditionalEffect.performEffects(self, event.context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)
                
    def findPossibleCards(self, context):
        """ Return the possible cards """
        source = context.loadSource(self.sourceType)
        possibleCards = source
        if self.filter is not None:
            possibleCards = self.filter.evaluate(context)
        
        return source, possibleCards
        
    def setNumberOfCards(self, number):
        """ Set the Number of Cards that can be requested """
        self.numberOfCards = number