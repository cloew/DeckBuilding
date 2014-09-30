from request import Request

from Game.Effects.Conditions.Filters.comparison_filter import ComparisonFilter
from Game.Effects.Conditions.Filters.Criteria.fixed_criteria import FixedCriteria
from Game.Sources.source_factory import HAND

class DefendRequest(Request):
    """ Represents a Request to Defend """
    
    def __init__(self, attackCard, target, args):
        """ Initialize the Request with the attack """
        self.attackCard = attackCard
        self.args = args.copy()
        self.args.player = target
        self.defenseRequest = ComparisonFilter(HAND, FixedCriteria("isDefense", True, "=="))
        Request.__init__(self, [target])
        
    @property
    def defenses(self):
        """ Return the relevant source if any """
        args = self.args.copy()
        args.parent = None
        return self.defenseRequest.evaluate(args)