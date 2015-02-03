from Game.Commands.Requests.choose_option_request import ChooseOptionRequest
from Game.Effects.effect_runner import PerformEffect
from Game.Effects.choice import Choice, Option
from Game.Effects.per_match import PerMatch
from Game.Effects.Conditions.Filters.comparison_filter import ComparisonFilter
from Game.Effects.Conditions.Filters.intersection_filter import IntersectionFilter
from Game.Effects.Conditions.Filters.unique_filter import UniqueFilter
from Game.Effects.Conditions.Filters.Criteria.fixed_criteria import FixedCriteria
from Game.Events.cards_event import CardsEvent

class PickType:
    """ Represents an effect that applies for each matching card """
    
    def __init__(self, zoneType, effects, filter=None):
        """ Initialize the Effect with the condition to evaluate and effect to perform """
        self.zoneType = zoneType
        self.effects = effects
        self.filter = filter
        
        self.cardTypeFilter = IntersectionFilter([UniqueFilter("cardType", self.zoneType), self.filter])
        
    def perform(self, context):
        """ Perform the Game Effect """
        choice = Choice(self.buildOptions(context), relevantZoneType=self.zoneType, filter=self.filter)
        coroutine = PerformEffect(choice, context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)
                
    def buildOptions(self, context):
        """ Build the Options for the card types """
        options = []
        for cardType in self.findPossibleTypes(context):
            cardFilter = IntersectionFilter([self.filter, ComparisonFilter(self.zoneType, FixedCriteria("cardType", cardType, "=="))])
            options.append(Option("Pick " + cardType, [PerMatch(self.zoneType, self.effects, filter=cardFilter)]))
        return options
                
    def findPossibleTypes(self, context):
        """ Initialize the Possible Types """
        return [card.cardType for card in self.cardTypeFilter.evaluate(context)]
                
    def findPossibleCards(self, context):
        """ Return the possible cards """
        zone = context.loadZone(self.zoneType)
        possibleCards = zone
        if self.filter is not None:
            possibleCards = self.filter.evaluate(context)
        
        return zone, possibleCards