from Game.Effects.add_trigger import AddTrigger
from Game.Effects.conditional_effect import ConditionalEffect
from Game.Effects.Conditions.and_condition import AndCondition
from Game.Effects.Conditions.matching import Matching
from Game.Effects.Triggers.trigger import Trigger
from Game.Sources.source_factory import PLAYED, EVENT

class PlayOrHavePlayed(ConditionalEffect):
    """ Represents an effect that conditionally applies """
    
    def __init__(self, effect, criteria):
        """ Initialize the Effect with the condition to evaluate and effect to perform """
        playedCondition = Matching(PLAYED, criteria)
        eventCondition = Matching(EVENT, criteria)
        triggerCondition = AndCondition([playedCondition, eventCondition])
        
        trigger = Trigger("CARD_PLAYED", triggerCondition, effect, singleUse=True)
        ConditionalEffect.__init__(self, playedCondition, effect, otherwiseEffect=AddTrigger(trigger))