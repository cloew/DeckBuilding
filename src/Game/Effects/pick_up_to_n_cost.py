from Game.Commands.Requests.pick_up_to_n_cost_request import PickUpToNCostRequest
from Game.Effects.pick_cards import PickCards
from Game.Effects.Conditions.Filters.Criteria.fixed_criteria import FixedCriteria

class PickUpToNCost(PickCards):
    """ Represents an effect to pick up to some number cards from a zone and an optional filter """
    REQUEST_CLASS = PickUpToNCostRequest
    AUTO_PICK = False
    
    def __init__(self, zoneTypes, cost, toDescription, thenEffects, leftoverCardEffects=[]):
        """ Initialize the options """
        self.cost = cost
        PickCards.__init__(self, zoneTypes, 1, toDescription, thenEffects, criteria=[FixedCriteria("cost", self.cost, "<=")], leftoverCardEffects=[])
        
    def buildRequest(self, possibleCards, context):
        """ Build the Request """
        return self.REQUEST_CLASS([card for card in possibleCards if card.cost <= self.cost], context.player, self.cost, self.toDescription)