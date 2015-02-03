from Game.Effects.add_trigger import AddTrigger
from Game.Effects.conditional_effect import ConditionalEffect
from Game.Effects.Conditions.matching import Matching
from Game.Effects.Triggers.trigger import Trigger
from Game.Events.game_events import CARD_PLAYED
from Game.Zones.zone_types import PLAYED, EVENT

class PlayOrHavePlayed(ConditionalEffect):
    """ Represents an effect that conditionally applies """
    
    def __init__(self, effect, criteria):
        """ Initialize the Effect with the condition to evaluate and effect to perform """
        playedCondition = Matching(PLAYED, criteria)
        eventCondition = Matching(EVENT, criteria)
            
        addTriggerEffect = self.buildTriggerEffect(playedCondition, eventCondition, effect)
        effects = [effect]
            
        ConditionalEffect.__init__(self, playedCondition, effects, otherwiseEffect=addTriggerEffect)
        
    def buildTriggerEffect(self, playedCondition, eventCondition, effect):
        """ Build the Trigger Effect to be used """
        triggerCondition = self.getTriggerCondition(playedCondition, eventCondition)
        trigger = Trigger(CARD_PLAYED, effect, condition=triggerCondition, singleUse=True)
        return AddTrigger(trigger)
    
    def getTriggerCondition(self, playedCondition, eventCondition):
        """ Get the Condition for the Trigger """
        return eventCondition
        