from Game.Effects.add_trigger import AddTrigger
from Game.Effects.effect_runner import PerformEffects
from Game.Effects.per_match import PerMatch
from Game.Effects.Conditions.matching import Matching
from Game.Effects.Conditions.Filters.comparison_filter import ComparisonFilter
from Game.Effects.Triggers.trigger import Trigger
from Game.Events.game_events import CARD_PLAYED
from Game.Sources.source_types import PLAYED, EVENT

class ForAllPlayOrHavePlayed:
    """ Represents an effect that performs for all cards matching some criteria that have been played or will be played """
    
    def __init__(self, effect, criteria):
        """ Initialize the Effect with the condition to evaluate and effect to perform """
        perMatchEffect = PerMatch(PLAYED, [effect], filter=ComparisonFilter(PLAYED, criteria))
        addTriggerEffect = self.buildTriggerEffect(effect, criteria)
        self.effects = [perMatchEffect, addTriggerEffect]
        
    def perform(self, context):
        """ Perform the Game Effect """
        coroutine = PerformEffects(self.effects, context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)
        
    def buildTriggerEffect(self, effect, criteria):
        """ Build the Trigger Effect to be used """
        triggerCondition = Matching(EVENT, criteria)
        trigger = Trigger(CARD_PLAYED, effect, condition=triggerCondition, singleUse=False)
        return AddTrigger(trigger)
    
    def getTriggerCondition(self, playedCondition, eventCondition):
        """ Get the Condition for the Trigger """
        return eventCondition
        