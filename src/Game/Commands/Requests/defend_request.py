from request import Request

from Game.Effects.Conditions.Filters.comparison_filter import ComparisonFilter
from Game.Effects.Conditions.Filters.Criteria.fixed_criteria import FixedCriteria
from Game.Sources.source_types import HAND, ONGOING

class DefendRequest(Request):
    """ Represents a Request to Defend """
    SOURCES = [HAND, ONGOING]
    
    def __init__(self, attackCard, context):
        """ Initialize the Request with the attack """
        self.attackCard = attackCard
        self.context = context
        self.defenseFilters = [ComparisonFilter(sourceType, FixedCriteria("defendFrom", sourceType, "==")) for sourceType in self.SOURCES]
        self.cardsForSource = {}
        Request.__init__(self, [context.player])
        
    @property
    def defenses(self):
        """ Return the relevant source if any """
        context = self.context.copy()
        context.parent = None
        cards = []
        for i, filter in enumerate(self.defenseFilters):
            results = filter.evaluate(context)
            self.cardsForSource[self.SOURCES[i]] = results
            cards += results
        return cards
        
    def findSourceFor(self, card):
        """ Find the source for the card """
        for sourceType in self.SOURCES:
            if card in self.cardsForSource[sourceType]:
                return sourceType
        return None