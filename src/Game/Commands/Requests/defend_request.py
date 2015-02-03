from request import Request

from Game.Effects.Conditions.Filters.comparison_filter import ComparisonFilter
from Game.Effects.Conditions.Filters.Criteria.fixed_criteria import FixedCriteria
from Game.Zones.zone_types import HAND, ONGOING

class DefendRequest(Request):
    """ Represents a Request to Defend """
    ZONES = [HAND, ONGOING]
    
    def __init__(self, attackCard, context):
        """ Initialize the Request with the attack """
        self.attackCard = attackCard
        self.context = context
        self.defenseFilters = [ComparisonFilter(zoneType, FixedCriteria("defendFrom", zoneType, "==")) for zoneType in self.ZONES]
        self.cardsForZone = {}
        Request.__init__(self, [context.player])
        
    @property
    def defenses(self):
        """ Return the relevant zone if any """
        context = self.context.copy()
        context.parent = None
        cards = []
        for i, filter in enumerate(self.defenseFilters):
            results = filter.evaluate(context)
            self.cardsForZone[self.ZONES[i]] = results
            cards += results
        return cards
        
    def findZoneFor(self, card):
        """ Find the zone for the card """
        for zoneType in self.ZONES:
            if card in self.cardsForZone[zoneType]:
                return zoneType
        return None