from Game.Effects.add_trigger import AddTrigger
from Game.Effects.conditional_effect import ConditionalEffect
from Game.Effects.Conditions.matching import Matching
from Game.Effects.Triggers.trigger import Trigger
from Game.Sources.source_types import PLAYED, EVENT

class PlayOrHavePlayed(ConditionalEffect):
    """ Represents an effect that conditionally applies """
    
    def __init__(self, effect, criteria, singleUse=None):
        """ Initialize the Effect with the condition to evaluate and effect to perform """
        playedCondition = Matching(PLAYED, criteria)
        eventCondition = Matching(EVENT, criteria)
        triggerCondition = self.getTriggerCondition(playedCondition, eventCondition)
        
        if singleUse is None:
            singleUse = True
        trigger = Trigger("CARD_PLAYED", effect, condition=triggerCondition, singleUse=singleUse)
        ConditionalEffect.__init__(self, playedCondition, [effect], otherwiseEffect=AddTrigger(trigger))
        
    def getTriggerCondition(self, playedCondition, eventCondition):
        """ Get the Condition for the Trigger """
        return eventCondition